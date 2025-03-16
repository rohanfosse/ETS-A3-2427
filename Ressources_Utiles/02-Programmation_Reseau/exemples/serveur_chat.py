import socket
import threading

clients = []

def gerer_client(client_socket, client_address):
    """Gère un client et diffuse ses messages aux autres."""
    print(f"Nouvelle connexion : {client_address}")
    clients.append(client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"{client_address} : {message}")
            envoyer_a_tous(message, client_socket)
        except:
            break

    print(f"Connexion fermée : {client_address}")
    clients.remove(client_socket)
    client_socket.close()

def envoyer_a_tous(message, sender_socket):
    """Envoie le message à tous les clients sauf l'expéditeur."""
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode())
            except:
                pass

# Démarrage du serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("127.0.0.1", 12345))
serveur.listen(5)

print("Serveur de chat démarré...")

while True:
    client_socket, client_address = serveur.accept()
    thread = threading.Thread(target=gerer_client, args=(client_socket, client_address))
    thread.start()
