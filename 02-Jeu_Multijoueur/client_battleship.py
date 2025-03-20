import socket
import json

# Configuration client
HOST = 'localhost'
PORT = 65432

def se_connecter_au_serveur():
    """Établir la connexion avec le serveur."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    return client_socket

def envoyer_tir(client_socket, coordonnees):
    """Envoyer les coordonnées du tir au serveur."""
    pass

def recevoir_etat(client_socket):
    """Recevoir et traiter les mises à jour du jeu depuis le serveur."""
    pass

def afficher_grille(etat):
    """Afficher la grille de jeu mise à jour."""
    pass

def main():
    """Boucle principale du client."""
    client_socket = se_connecter_au_serveur()

    try:
        while True:
            etat = recevoir_etat(client_socket)
            afficher_grille(etat)

            coordonnees = input("Entrez les coordonnées de votre tir (ligne,colonne) : ")
            envoyer_tir(client_socket, coordonnees)

    except KeyboardInterrupt:
        print("\nDéconnexion du serveur.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
