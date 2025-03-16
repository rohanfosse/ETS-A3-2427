import socket
import threading
import random
import json
import time
import os
import signal
import sys

class ServeurDefiMot:
    def __init__(self, host, port, fichier_mots):
        self.host = host
        self.port = port
        self.clients = {}  # {conn: nom_joueur}
        self.scores = {}
        self.mots = self.charger_mots(fichier_mots)
        self.mot_actuel = ""
        self.lettres_essayees = []
        self.temps_restant = 120  # 2 minutes
        self.lock = threading.Lock()
        self.partie_en_cours = False
        self.running = True

    def charger_mots(self, fichier_mots):
        """
        Charge les mots depuis un fichier texte.
        """
        try:
            with open(fichier_mots, "r") as f:
                mots = [mot.strip().upper() for mot in f.readlines()]
                if not mots:
                    raise ValueError("Le fichier de mots est vide.")
                print(f"📖 {len(mots)} mots chargés depuis {fichier_mots}")
                return mots
        except FileNotFoundError:
            print(f"❌ Erreur : Le fichier {fichier_mots} n'existe pas.")
            exit(1)

    def choisir_nouveau_mot(self):
        """
        Choisit un nouveau mot mystère et réinitialise les lettres essayées.
        """
        with self.lock:
            if not self.mots:  # Vérifier si la liste des mots est vide
                print("❌ Erreur : Aucun mot disponible dans la liste !")
                return

            self.mot_actuel = random.choice(self.mots)  # Sélectionner un mot aléatoire
            self.lettres_essayees = []

            print(f"🔒 Nouveau mot mystère choisi : {self.mot_actuel}")  # DEBUG (à cacher aux joueurs)


    def gerer_client(self, conn, addr):
        """
        Gère la communication avec un client.
        """
        try:
            data = conn.recv(1024).decode().strip()
            action = json.loads(data)
            if action["type"] != "connexion":
                raise ValueError("⚠️ Mauvais format de connexion.")

            nom_joueur = action["nom"]
            with self.lock:
                self.clients[conn] = nom_joueur
                self.scores[nom_joueur] = 0
            
            print(f"✅ {nom_joueur} connecté depuis {addr}")
            self.diffuser_etat()  # Envoyer l'état initial au nouveau client

            while True:
                data = conn.recv(1024).decode().strip()
                if not data:
                    break

                try:
                    action = json.loads(data)
                    self.traiter_action(nom_joueur, action)
                except json.JSONDecodeError:
                    print(f"⚠️ Erreur JSON reçu de {nom_joueur} : {data}")

        except Exception as e:
            print(f"❌ Erreur avec le client {addr} : {e}")
        
        finally:
            with self.lock:
                nom_joueur = self.clients.pop(conn, "Inconnu")
                if nom_joueur in self.scores:
                    del self.scores[nom_joueur]
            conn.close()
            print(f"❌ {nom_joueur} déconnecté.")
            self.diffuser_etat()

    def traiter_action(self, joueur, action):
        """
        Traite une action envoyée par un joueur.
        """
        with self.lock:
            reponse = {}

            if action["type"] == "lettre":
                lettre = action["valeur"].upper()
                print(f"🔠 {joueur} propose la lettre '{lettre}'.")

                if not self.mot_actuel:  # Vérifier si le mot est défini
                    print("❌ ERREUR : Aucun mot n'est défini !")
                    self.choisir_nouveau_mot()

                if lettre in self.lettres_essayees:
                    print(f"⚠️ Lettre déjà essayée.")
                    reponse = {"type": "erreur", "message": f"Lettre '{lettre}' déjà tentée."}
                elif lettre in self.mot_actuel:
                    self.lettres_essayees.append(lettre)
                    print(f"✅ Lettre correcte !")
                    reponse = {"type": "confirmation", "message": f"Lettre '{lettre}' correcte !"}
                else:
                    print(f"❌ Lettre incorrecte.")
                    reponse = {"type": "erreur", "message": f"Lettre '{lettre}' incorrecte."}

            elif action["type"] == "mot":
                mot_propose = action["valeur"].upper()
                print(f"📝 {joueur} propose le mot '{mot_propose}'.")

                if not self.mot_actuel:
                    print("❌ ERREUR : Aucun mot n'est défini !")
                    self.choisir_nouveau_mot()

                if mot_propose == self.mot_actuel:
                    print(f"🎉 {joueur} a trouvé le mot mystère '{self.mot_actuel}' !")
                    self.scores[joueur] += 1
                    reponse = {"type": "gagne", "message": f"🏆 {joueur} a trouvé le mot '{self.mot_actuel}' !"}
                    time.sleep(2)  # Pause avant de changer de mot
                    self.choisir_nouveau_mot()  # 🔥 CHANGER LE MOT APRÈS VICTOIRE !
                else:
                    print(f"❌ Mot incorrect.")
                    reponse = {"type": "erreur", "message": "Mauvaise réponse, essayez encore."}

            elif action["type"] == "deconnexion":
                print(f"👋 {joueur} quitte la partie.")
                reponse = {"type": "info", "message": f"{joueur} a quitté la partie."}

            else:
                print(f"⚠️ Action inconnue reçue : {action}")
                reponse = {"type": "erreur", "message": "Action non reconnue."}

            # Envoyer la réponse spécifique au joueur qui a joué
            for client, nom in self.clients.items():
                if nom == joueur:
                    try:
                        client.sendall((json.dumps(reponse) + "\n").encode())
                    except:
                        print(f"❌ Impossible d'envoyer la réponse à {joueur}")

            # 📢 Diffuser l'état du jeu mis à jour après chaque action !
            self.diffuser_etat()



    def diffuser_etat(self):
        """
        Diffuse l'état actuel du jeu à tous les clients.
        """
        with self.lock:
            if not self.mot_actuel:  # Vérifier si le mot est bien défini
                print("❌ Aucun mot mystère défini ! On choisit un nouveau mot.")
                self.choisir_nouveau_mot()

            etat_jeu = {
                "mot_actuel": "".join([lettre if lettre in self.lettres_essayees else "_" for lettre in self.mot_actuel]),
                "scores": self.scores,
                "temps_restant": self.temps_restant,
            }

            message = json.dumps(etat_jeu) + "\n"

            print(f"📡 Diffusion de l'état du jeu : {etat_jeu}")  # Ajout pour debug

            for client in list(self.clients.keys()):
                try:
                    client.sendall(message.encode())
                except:
                    print(f"❌ Erreur lors de l'envoi à {self.clients[client]}")
                    client.close()
                    del self.clients[client]




    def diffuser_message(self, message):
        """
        Envoie un message JSON à tous les clients connectés.
        """
        message_str = json.dumps(message) + "\n"
        with self.lock:
            for client in list(self.clients.keys()):
                try:
                    client.sendall(message_str.encode())
                except:
                    print(f"❌ Erreur lors de l'envoi à {self.clients[client]}.")
                    client.close()
                    del self.clients[client]

    def lancer_partie(self):
        """
        Gère le chronomètre de la partie.
        """
        print("🚀 Lancement de la partie...")
        with self.lock:
            if not self.clients:
                print("❌ Aucun joueur connecté. La partie ne peut pas démarrer.")
                return
            
            self.choisir_nouveau_mot()
        
        while self.temps_restant > 0 and self.running:
            time.sleep(1)
            with self.lock:
                self.temps_restant -= 1
            
            self.diffuser_etat()

        print("⏳ Temps écoulé. Fin de la partie.")
        self.diffuser_message({"type": "fin_partie", "message": "⏳ Temps écoulé. Fin du jeu !"})

    def arreter(self):
        """
        Arrête proprement le serveur et ferme les connexions.
        """
        print("\n🛑 Arrêt du serveur...")

        with self.lock:
            self.running = False  # Stopper la boucle principale

            # 🔥 Fermer toutes les connexions clients proprement
            for client in list(self.clients.keys()):
                try:
                    client.sendall(json.dumps({"type": "fin_partie", "message": "🔴 Le serveur s'arrête."}).encode())
                    client.close()
                except Exception as e:
                    print(f"⚠️ Erreur lors de la fermeture d'un client : {e}")

            self.clients.clear()
            self.scores.clear()

        # 🔥 Fermer le socket serveur
        try:
            if self.socket:
                self.socket.close()
                print("🔒 Socket serveur fermé.")
        except Exception as e:
            print(f"⚠️ Erreur lors de la fermeture du socket serveur : {e}")

        print("✅ Le serveur est maintenant arrêté.")
        sys.exit(0)  # 🔥 Forcer la fermeture du programme


    def demarrer(self):
        """
        Démarre le serveur et accepte les connexions des clients.
        """
        signal.signal(signal.SIGINT, self.signal_handler)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            self.socket = s  # 🔥 Garder une référence pour fermeture propre
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permettre le redémarrage immédiat
            s.bind((self.host, self.port))
            s.listen()
            print(f"✅ Serveur démarré sur {self.host}:{self.port}")

            while self.running:
                try:
                    s.settimeout(1)  # 🔥 Timeout pour éviter un blocage sur accept()
                    conn, addr = s.accept()
                    if not self.running:
                        break  # Arrêter immédiatement si le serveur doit fermer

                    threading.Thread(target=self.gerer_client, args=(conn, addr), daemon=True).start()

                    if not self.partie_en_cours:
                        self.choisir_nouveau_mot()
                        threading.Thread(target=self.lancer_partie, daemon=True).start()
                        self.partie_en_cours = True

                except socket.timeout:
                    continue  # 🔥 Vérifier régulièrement si le serveur doit s'arrêter
                except OSError:
                    break  # 🔥 Quitter si le socket a été fermé

            print("🛑 Serveur arrêté.")




    def signal_handler(self, signum, frame):
        """
        Gère l'arrêt du serveur via Ctrl+C.
        """
        print("\n🛑 Interruption par l'utilisateur (Ctrl+C).")
        self.arreter()


if __name__ == "__main__":
    chemin_script = os.path.dirname(os.path.abspath(__file__))
    chemin_fichier = os.path.join(chemin_script, "mots.txt")
    
    serveur = ServeurDefiMot("127.0.0.1", 12345, chemin_fichier)
    serveur.demarrer()
