import socket

# Création du socket TCP
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à une adresse IP et un port
serveur.bind(("127.0.0.1", 12345))

# Mettre le serveur en attente de connexions
serveur.listen(1)
print("Serveur en attente d'une connexion...")

# Accepter une connexion
client_socket, client_address = serveur.accept()
print(f"Connexion établie avec {client_address}")

# Envoyer un message au client
client_socket.sendall(b"Bienvenue sur le serveur !")

# Fermer la connexion
client_socket.close()
serveur.close()
