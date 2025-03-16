import socket
import threading

def gerer_client(client_socket, client_address):
    """Gère un client individuel."""
    print(f"Nouvelle connexion : {client_address}")
    client_socket.sendall(b"Bienvenue sur le serveur multi-clients !")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Message de {client_address} : {data.decode()}")
            client_socket.sendall("Message reçu")
        except ConnectionResetError:
            break

    print(f"Connexion fermée avec {client_address}")
    client_socket.close()

# Création du serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("127.0.0.1", 12345))
serveur.listen(5)  # Accepte jusqu'à 5 clients simultanément

print("Serveur en attente de connexions...")

while True:
    client_socket, client_address = serveur.accept()
    thread = threading.Thread(target=gerer_client, args=(client_socket, client_address))
    thread.start()
