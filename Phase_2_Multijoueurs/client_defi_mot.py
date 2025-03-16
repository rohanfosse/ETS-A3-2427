import socket
import json

class ClientDefiMot:
    def __init__(self, host, port):
        """
        Initialise le client avec l'adresse et le port du serveur.
        """
        self.host = host
        self.port = port
        self.socket = None

    def se_connecter(self):
        """
        Se connecte au serveur via sockets.
        """
        pass  # Indice : Utilisez socket.connect((host, port)).

    def envoyer_action(self, action):
        """
        Envoie une action au serveur (proposer une lettre ou un mot).
        :param action: Dictionnaire contenant l'action ("lettre" ou "mot").
                       Exemple: {"type": "lettre", "valeur": "A"}
                       Exemple: {"type": "mot", "valeur": "PYTHON"}
        """
        pass  # Indice : Convertissez l'action en JSON avant de l'envoyer via socket.send().

    def recevoir_etat_jeu(self):
        """
        Reçoit l'état actuel du jeu depuis le serveur.
        :return: Dictionnaire représentant l'état du jeu.
                 Exemple: {"mot_actuel": "_ A _ _ E", "scores": {"Joueur1": 3}, ...}
        """
        pass  # Indice : Utilisez socket.recv() pour recevoir une chaîne JSON et la convertir en dictionnaire.

    def jouer(self):
        """
        Boucle principale du client pour jouer au jeu.
        Affiche l'état actuel et permet d'envoyer des actions au serveur.
        """
        pass  # Indice : Recevez l'état du jeu, affichez-le, puis demandez à l'utilisateur d'entrer une action.

if __name__ == "__main__":
    client = ClientDefiMot("127.0.0.1", 12345)
    client.se_connecter()
    client.jouer()
