# **Exercice : Serveur de Chat avec Noms d’Utilisateurs**

## **Objectif**

Dans cet exercice, vous allez modifier un **serveur de chat multi-clients** pour que chaque utilisateur entre son **nom** avant d'envoyer des messages.

L’objectif est d’afficher les messages sous la forme :

```
Alice : Bonjour !
Bob : Salut Alice !
```

Au lieu de simplement :

```
Bonjour !
Salut Alice !
```

---

## **1. Fonctionnalités à Implémenter**

### **Côté Serveur (`serveur_exo.py`)**

1. **Demander le nom du client à la connexion** et l’enregistrer.
2. **Afficher les messages avec le nom du client**.
3. **Gérer plusieurs clients simultanément** avec des **threads**.
4. **Gérer les déconnexions proprement**.

### **Côté Client (`client_exo.py`)**

1. **Demander le nom de l’utilisateur au lancement**.
2. **Envoyer ce nom au serveur dès la connexion**.
3. **Permettre à l’utilisateur d’envoyer et recevoir des messages en continu**.
4. **Gérer la déconnexion en tapant `exit`**.

---

## **2. Exemples de Fonctionnement**

### **Côté Serveur**

Le serveur affiche les connexions et les messages :

```
Serveur en attente de connexions...
Alice (127.0.0.1) a rejoint le chat.
Bob (127.0.0.1) a rejoint le chat.
Alice : Bonjour !
Bob : Salut Alice !
Alice a quitté le chat.
```

---

### **Côté Client**

#### **Client Alice**

```
Entrez votre nom : Alice
Votre message : Bonjour !
```

#### **Client Bob**

```
Entrez votre nom : Bob
Votre message : Salut Alice !
```

---

## **3. Contraintes et Améliorations**

### **Contraintes**

- **Le serveur doit accepter plusieurs connexions simultanées**.
- **Les messages doivent être envoyés en UTF-8**.
- **Chaque message doit être affiché avec le nom de l’expéditeur**.

### **Améliorations possibles (Bonus)**

- Ajouter une **commande `/liste`** pour afficher les utilisateurs connectés.
- Ajouter un **horodatage (`[HH:MM]`)** devant chaque message.
- Ajouter un **système de commandes** (`/quitter`, `/privé` pour messages privés).
- Permettre **le stockage des messages dans un fichier**.
