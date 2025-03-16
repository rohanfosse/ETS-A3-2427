import socket

# Création du socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client.connect(("127.0.0.1", 12345))

print("Connecté au serveur ! Tapez 'exit' pour quitter.")

while True:
    message = input("Votre message : ")
    if message.lower() == "exit":
        break
    client.sendall(message.encode())
    reponse = client.recv(1024)
    print("Réponse du serveur :", reponse.decode())

# Fermeture de la connexion
client.close()
