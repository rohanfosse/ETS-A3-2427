import json

def charger_dictionnaire(fichier):
    """
    Charge un dictionnaire de mots depuis un fichier texte.
    :param fichier: Chemin vers le fichier contenant les mots.
    :return: Liste de mots.
    """
    with open(fichier, 'r') as f:
        return [mot.strip().upper() for mot in f.readlines()]

def envoyer_message(socket, message):
    """
    Envoie un message JSON via un socket.
    :param socket: Le socket sur lequel envoyer le message.
    :param message: Le message à envoyer (dictionnaire).
    """
    data = json.dumps(message)
    socket.sendall(data.encode())

def recevoir_message(socket):
    """
    Reçoit un message JSON via un socket.
    :param socket: Le socket depuis lequel recevoir le message.
    :return: Le message reçu (dictionnaire).
    """
    data = socket.recv(1024).decode()
    return json.loads(data)
