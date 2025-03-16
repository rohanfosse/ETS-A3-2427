import socket
import threading
import random
import time

class ServeurDefiMot:
    def __init__(self, host, port, fichier_mots):
        """
        Initialise le serveur avec l'adresse et le port.
        Charge les mots depuis le fichier.
        """
        self.host = host
        self.port = port
        self.mots = self.charger_mots(fichier_mots)
        self.clients = []
        self.etat_jeu = {
            "mot_actuel": "",
            "lettres_essayees": [],
            "scores": {},
            "temps_restant": 120,
        }
        self.lock = threading.Lock()

    def charger_mots(self, fichier_mots):
        """
        Charge les mots depuis un fichier texte.
        :param fichier_mots: Chemin vers le fichier contenant les mots.
        :return: Liste de mots.
        """
        pass  # Indice : Utilisez open() pour lire les mots ligne par ligne.

    def choisir_mot(self):
        """
        Sélectionne un mot aléatoire parmi ceux disponibles.
        """
        pass  # Indice : Utilisez random.choice() sur la liste des mots.

    def gerer_client(self, client_socket, adresse):
        """
        Gère les interactions avec un client spécifique.
        """
        pass  # Indice : Recevez les messages via client_socket.recv() et envoyez via client_socket.send().

    def diffuser_etat_jeu(self):
        """
        Envoie l'état actuel du jeu à tous les clients connectés.
        """
        pass  # Indice : Parcourez self.clients et envoyez l'état sous forme de chaîne JSON.

    def demarrer(self):
        """
        Démarre le serveur et accepte les connexions des clients.
        """
        pass  # Indice : Utilisez socket.bind(), socket.listen(), et acceptez les connexions avec socket.accept().

if __name__ == "__main__":
    serveur = ServeurDefiMot("127.0.0.1", 12345, "mots.txt")
    serveur.demarrer()
