import socket
import json
import time
import sys
import signal

class ClientDefiMot:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False
        self.timeout = 10  # Timeout en secondes pour la connexion et la réception des données
        self.running = True

    def se_connecter(self):
        """
        Connecte le client au serveur et envoie le nom du joueur.
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            print(f"Tentative de connexion au serveur {self.host}:{self.port}...")
            self.socket.connect((self.host, self.port))
            self.connected = True
            print("✅ Connecté au serveur.")

            # Demander le nom du joueur
            nom_joueur = input("Entrez votre nom : ").strip()
            if not nom_joueur:
                print("❌ Nom invalide. Déconnexion...")
                self.arreter()
                return False

            # Envoyer le nom sous forme JSON avec un délimiteur
            self.envoyer_message({"type": "connexion", "nom": nom_joueur})
            return True
        except Exception as e:
            print(f"❌ Erreur de connexion : {e}")
            return False

    def envoyer_message(self, message):
        """
        Envoie un message JSON au serveur avec un délimiteur de fin de message.
        """
        try:
            message_str = json.dumps(message) + "\n"  # Ajout du délimiteur
            self.socket.sendall(message_str.encode('utf-8'))
            print(f"📤 Message envoyé : {message}")
        except Exception as e:
            print(f"❌ Erreur lors de l'envoi du message : {e}")
            self.connected = False

    def recevoir_donnees(self):
        """
        Reçoit un message JSON du serveur. Attend jusqu'à la réception complète d'un message.
        """
        data = b""
        start_time = time.time()
        while self.running:
            try:
                chunk = self.socket.recv(1024)
                if not chunk:
                    raise ConnectionResetError("🔴 Connexion perdue avec le serveur")
                
                data += chunk
                if b"\n" in chunk:  # Vérifier si on a reçu un message complet
                    break

            except socket.timeout:
                if time.time() - start_time > self.timeout:
                    raise TimeoutError("⏳ Timeout en attendant les données du serveur")
            except Exception as e:
                print(f"❌ Erreur lors de la réception des données : {e}")
                self.connected = False
                raise

        try:
            return json.loads(data.decode('utf-8').strip())  # Décodage du JSON
        except json.JSONDecodeError:
            print("❌ Erreur de décodage JSON. Reçu :", data)
            return None

    def jouer(self):
        """
        Boucle principale du jeu.
        """
        signal.signal(signal.SIGINT, self.signal_handler)  # Gérer Ctrl+C proprement
        
        while self.running and self.connected:
            try:
                print("🟡 En attente de données du serveur...")
                data = self.recevoir_donnees()

                if not data:
                    continue

                if data.get("type") == "fin_partie":
                    print("🏁 La partie est terminée.")
                    break

                print(f"\n🟢 Mot actuel : {data.get('mot_actuel', 'N/A')}")
                print(f"📊 Scores : {data.get('scores', {})}")
                print(f"⏳ Temps restant : {data.get('temps_restant', 'N/A')}s")

                action_type = input("\n🔠 Proposer une lettre (L) ou un mot entier (M) ? ").strip().upper()
                if action_type == "L":
                    lettre = input("✏️ Entrez une lettre : ").strip().upper()
                    if lettre and lettre.isalpha():
                        self.envoyer_message({"type": "lettre", "valeur": lettre})
                    else:
                        print("❌ Entrée invalide.")
                elif action_type == "M":
                    mot = input("✏️ Entrez un mot : ").strip().upper()
                    if mot:
                        self.envoyer_message({"type": "mot", "valeur": mot})
                    else:
                        print("❌ Entrée invalide.")
                else:
                    print("❌ Action invalide.")

            except (TimeoutError, ConnectionResetError):
                print("🔴 Déconnexion. Tentative de reconnexion...")
                if not self.se_connecter():
                    break
            except Exception as e:
                print(f"❌ Erreur inattendue : {e}")
                break

        self.arreter()

    def arreter(self):
        """
        Déconnecte proprement le client.
        """
        print("\n🔴 Déconnexion du serveur...")
        self.running = False
        if self.socket:
            try:
                self.envoyer_message({"type": "deconnexion"})
            except:
                pass  # Ignorer les erreurs à la fermeture
            finally:
                self.socket.close()

    def signal_handler(self, signum, frame):
        """
        Gère l'arrêt via Ctrl+C.
        """
        print("\n🛑 Interruption par l'utilisateur (Ctrl+C).")
        self.arreter()


if __name__ == "__main__":
    client = ClientDefiMot("127.0.0.1", 12345)
    if client.se_connecter():
        client.jouer()
    else:
        print("❌ Impossible de se connecter au serveur. Fin du programme.")
