import socket

# Création du socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client.connect(("127.0.0.1", 12345))

# Recevoir le message du serveur
message = client.recv(1024)
print("Message reçu :", message.decode())

# Fermer la connexion
client.close()
