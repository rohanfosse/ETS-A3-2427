# **Mini-Projet : Gestion d'une Bibliothèque en POO**  

## **Objectif**  

Ce mini-projet a pour but de mettre en pratique les notions avancées de **Programmation Orientée Objet (POO) en Python** à travers la création d’un **système de gestion de bibliothèque**. Vous devrez :  

- Gérer un catalogue de **livres**.  
- Permettre à des **utilisateurs** d’emprunter et de rendre des livres.  
- Appliquer des principes avancés de **POO** : **encapsulation, héritage, polymorphisme, composition, classes abstraites et design patterns**.  

Ce projet doit être structuré de manière **claire et modulaire**, en respectant les bonnes pratiques de conception logicielle.  

---

## **1. Structure attendue du projet**  

L’organisation du projet devra respecter la structure suivante :  

```
exercices/
│── bibliotheque.py          # Classe principale de gestion
│── livre.py                 # Classe Livre (Encapsulation)
│── utilisateur.py           # Classe Utilisateur (Héritage)
│── emprunt.py               # Gestion des emprunts (Composition)
│── singleton_config.py      # Singleton pour la configuration
│── factory_utilisateurs.py  # Factory pour créer des utilisateurs
│── main.py                  # Fichier principal d'exécution
│── README.md                # Explication du projet
```

---

## **2. Détails des fonctionnalités à implémenter**  

### **📌 1. Classe `Livre` (Encapsulation)**

- Chaque livre doit contenir au minimum un **titre**, un **auteur** et un **état de disponibilité**.  
- L’état de disponibilité ne doit **pas être modifiable directement** depuis l’extérieur.  
- Implémentez des méthodes permettant d’**emprunter** et de **rendre** un livre en modifiant son état.  

---

### **📌 2. Classe `Utilisateur` (Héritage et Polymorphisme)**

- Définissez une **classe parent `Utilisateur`** qui contiendra les informations générales d’un utilisateur (nom, liste d’emprunts).  
- Implémentez deux classes **`Etudiant` et `Professeur`** qui hériteront de `Utilisateur` et auront des **règles différentes** concernant le nombre maximum de livres empruntés.  
- Le nombre maximum d’emprunts devra être défini via **une méthode polymorphique** surchargée dans chaque classe enfant.  

---

### **📌 3. Gestion des Emprunts (Composition)**

- Implémentez une **classe `Emprunt`** qui représentera un **livre emprunté par un utilisateur**.  
- Cette classe devra permettre d’**assurer le lien entre un utilisateur et un livre**.  
- Elle devra contenir une **méthode permettant de retourner un livre** et de rétablir son état à "disponible".  

---

### **📌 4. Classe `Bibliotheque`**

- Cette classe sera responsable de la **gestion des livres et des utilisateurs**.  
- Elle devra permettre d’**ajouter de nouveaux livres** et de **gérer les emprunts**.  
- Implémentez une méthode permettant de **rechercher un livre** par son titre.  

---

### **📌 5. Singleton : Configuration de la Bibliothèque**

- Implémentez un **design pattern Singleton** pour stocker la configuration unique de la bibliothèque (ex. nom, nombre de livres maximum par défaut, etc.).  
- Assurez-vous que **seule une instance de cette classe puisse exister**.  

---

### **📌 6. Factory : Création Dynamique d’Utilisateurs**

- Utilisez un **pattern Factory** pour **créer des utilisateurs** (étudiants ou professeurs) sans exposer directement leurs classes.  
- La factory devra prendre en **paramètre le type d’utilisateur** et **retourner une instance de la bonne classe**.  

---

## **3. Contraintes et Bonnes Pratiques**

✔ **Encapsulation** : Les données sensibles ne doivent **pas être modifiables directement**.  
✔ **Héritage et polymorphisme** : Les classes `Etudiant` et `Professeur` doivent surcharger une méthode de `Utilisateur`.  
✔ **Composition** : L’objet `Emprunt` doit assurer la gestion entre `Livre` et `Utilisateur`.  
✔ **Utilisation de classes abstraites** (`ABC`) pour garantir la structure des classes.  
✔ **Utilisation des design patterns** (`Singleton` et `Factory`) pour organiser la gestion de la bibliothèque.  
✔ **Code modulaire et structuré** : Chaque fichier doit contenir **une seule responsabilité**.  

---

## **4. Exécution attendue (`main.py`)**  

Votre programme principal devra permettre de :  

1. **Créer une bibliothèque**.  
2. **Ajouter des livres** à la bibliothèque.  
3. **Créer des utilisateurs** via la **factory**.  
4. **Permettre aux utilisateurs d’emprunter des livres**.  
5. **Afficher les informations des utilisateurs et de leurs emprunts**.  
6. **Gérer le retour des livres** pour les rendre de nouveau disponibles.  

---

## **5. Extensions possibles (optionnel)**

Si vous souhaitez aller plus loin, voici quelques améliorations possibles :

- **Ajout d’une base de données** pour stocker les livres et utilisateurs.
- **Ajout d’un système de réservation** permettant aux utilisateurs de réserver un livre déjà emprunté.
- **Ajout d’une interface graphique** en utilisant `Tkinter` ou `PyQt`.
- **Gestion des pénalités** pour les utilisateurs rendant un livre en retard.
