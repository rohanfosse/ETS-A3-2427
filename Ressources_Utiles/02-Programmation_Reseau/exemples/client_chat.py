import socket
import threading

def recevoir_messages(client_socket):
    """Écoute les messages entrants du serveur et les affiche."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print("\nMessage reçu :", message)
        except:
            break

# Création du socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

# Démarrer un thread pour recevoir les messages du serveur
thread = threading.Thread(target=recevoir_messages, args=(client,))
thread.start()

# Envoi de messages en continu
while True:
    message = input("Votre message : ")
    if message.lower() == "exit":
        break
    client.sendall(message.encode())

client.close()
