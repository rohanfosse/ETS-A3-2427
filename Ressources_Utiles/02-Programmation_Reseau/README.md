# **Programmation Réseau avec Sockets et Threads en Python**

## **Introduction**

La programmation réseau permet aux applications de communiquer entre elles via un réseau local ou Internet. **Les sockets** sont la base de ces communications et permettent d’envoyer et de recevoir des données entre machines.

Dans ce guide, nous allons voir :

- **Les bases des sockets en Python**
- **Les différences entre TCP et UDP**
- **La création d’un serveur et d’un client en TCP**
- **L’utilisation des threads pour gérer plusieurs connexions simultanées**
- **Un exercice d’application**

---

## **1. Qu’est-ce qu’un Socket ?**

Un **socket** est un point de communication permettant à deux programmes de s’échanger des données sur un réseau.

Un socket suit généralement ces étapes :

1. **Création** : Un programme crée un socket.
2. **Connexion** : Il se connecte à un autre programme (client-serveur).
3. **Échange** : Les données sont envoyées et reçues.
4. **Fermeture** : Le socket est fermé après utilisation.

---

## **2. TCP vs UDP : Quelle Différence ?**

Il existe deux principaux types de protocoles pour les sockets :

| Protocole | Fonctionnement | Avantages | Inconvénients |
|-----------|---------------|-----------|--------------|
| **TCP** (Transmission Control Protocol) | Connexion fiable avec contrôle des erreurs. | Sécurisé, garantit que les données arrivent complètes et dans l’ordre. | Plus lent, nécessite une connexion. |
| **UDP** (User Datagram Protocol) | Envoie les messages sans vérifier leur réception. | Rapide, utilisé pour les communications temps réel. | Pas de garantie d’arrivée ni d’ordre des messages. |

Dans la plupart des cas, **TCP** est utilisé pour les applications nécessitant des **données fiables**, tandis que **UDP** est privilégié pour des applications où la rapidité est essentielle.

---

## **3. Création d’un Serveur TCP**

Un serveur doit :

1. **Créer un socket et l’attacher à une adresse et un port.**
2. **Écouter les connexions entrantes.**
3. **Accepter les connexions et échanger des messages.**
4. **Fermer la connexion lorsque nécessaire.**

Voici un **serveur TCP simple** :

### **Fichier : `serveur.py`**

```python
import socket

# Création du socket TCP
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attachement à une adresse et un port
serveur.bind(("127.0.0.1", 12345))
serveur.listen(1)  # Attente d'une connexion

print("Serveur en attente d'une connexion...")

# Acceptation d'un client
client_socket, client_address = serveur.accept()
print(f"Connexion établie avec {client_address}")

# Envoi d'un message
client_socket.sendall(b"Bienvenue sur le serveur !")

# Fermeture de la connexion
client_socket.close()
serveur.close()
```

---

## **4. Création d’un Client TCP**

Le client doit :

1. **Créer un socket.**
2. **Se connecter au serveur.**
3. **Échanger des messages.**
4. **Fermer la connexion.**

Voici un **client TCP simple** :

### **Fichier : `client.py`**

```python
import socket

# Création du socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client.connect(("127.0.0.1", 12345))

# Réception du message
message = client.recv(1024)  # 1024 octets max
print("Message reçu :", message.decode())

# Fermeture de la connexion
client.close()
```

---

## **5. Gestion de Plusieurs Clients avec les Threads**

Un **serveur basique** ne peut gérer qu’une seule connexion à la fois. Pour permettre **plusieurs connexions simultanées**, on utilise **les threads**.

Chaque client est géré dans un **thread séparé**, ce qui permet d'exécuter plusieurs connexions en parallèle.

### **Serveur Multi-Clients avec Threads**

Nous allons modifier le serveur pour :

1. **Accepter plusieurs clients**.
2. **Créer un thread pour chaque client**.
3. **Écouter les messages envoyés par chaque client.**

#### **Fichier : `serveur_multi.py`**

```python
import socket
import threading

def gerer_client(client_socket, client_address):
    print(f"Connexion établie avec {client_address}")
    client_socket.sendall(b"Bienvenue sur le serveur!")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break  # Fin de connexion
            print(f"Message de {client_address} : {data.decode()}")
            client_socket.sendall(b"Message reçu")
        except ConnectionResetError:
            break  # Gestion de la déconnexion brutale

    print(f"Connexion fermée avec {client_address}")
    client_socket.close()

# Création du serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("127.0.0.1", 12345))
serveur.listen(5)  # Accepte jusqu'à 5 clients

print("Serveur en attente de connexions...")

while True:
    client_socket, client_address = serveur.accept()
    thread = threading.Thread(target=gerer_client, args=(client_socket, client_address))
    thread.start()
```

Grâce aux **threads**, chaque client est géré indépendamment et peut envoyer des messages sans bloquer les autres.

---

## **6. Exemple d’Application : Chat Basique**

Voici un exemple où un **serveur de chat** envoie et reçoit des messages de plusieurs clients en simultané.

### **Serveur de Chat**

```python
import socket
import threading

clients = []

def gerer_client(client_socket, client_address):
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
```

### **Client de Chat**

```python
import socket
import threading

def recevoir_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print("\nMessage reçu :", message)
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

thread = threading.Thread(target=recevoir_messages, args=(client,))
thread.start()

while True:
    message = input("Votre message : ")
    client.sendall(message.encode())
```

---

## **7. Exercice d’Application**

**Objectif** : Modifier le serveur et le client pour **envoyer un nom d’utilisateur** lors de la connexion et l’afficher avec chaque message.

### **Instructions**

1. Le **client** doit demander un **nom d’utilisateur** avant d’envoyer des messages.
2. Le **serveur** doit afficher les messages avec le nom d’utilisateur du client.
3. Chaque message reçu doit être précédé du nom d’utilisateur de l’expéditeur.

### **Question Bonus**

- Comment pourrait-on **ajouter un historique des messages** stocké sur le serveur ?

---

## **8. Conclusion**

- **Les sockets permettent la communication réseau en Python**.
- **TCP assure une connexion fiable** entre un serveur et plusieurs clients.
- **Les threads permettent de gérer plusieurs connexions simultanément**.
- **Un chat multi-clients est une bonne application pour s’entraîner aux sockets.**

Pour aller plus loin, essayez d’implémenter un **système de notifications**, un **serveur en UDP**, ou une **interface graphique pour le chat**.
