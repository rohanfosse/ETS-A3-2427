# 🚢 **Mini-Projet de Validation – "Battle Ship Royale Solo"**

## **Contexte**

Ce projet consiste à développer une version solo du jeu **Battle Ship Royale**, dans lequel le joueur affronte un adversaire virtuel simple.

- Le joueur place ses bateaux sur une grille de jeu.
- Le joueur et l'adversaire virtuel tirent à tour de rôle pour tenter de couler les bateaux adverses.
- Chaque tir touche ou rate, et l'objectif est de couler tous les bateaux adverses en premier.
- Une gestion visuelle simplifiée de la grille permet au joueur de suivre l'état du jeu.
- Le score final est basé sur le nombre de tirs nécessaires pour couler tous les bateaux adverses.

Ce projet doit être réalisé **en autonomie** en complétant le code fourni.

[Voir les consignes détaillées](Phase_1_Fondamentaux/Phase_1_Consignes.md)

---

## **Objectifs pédagogiques**

- **Manipuler des structures de données** : listes, matrices, dictionnaires.
- **Utiliser les boucles et conditions pour gérer un jeu interactif**.
- **Implémenter la logique de placement et de gestion des bateaux**.
- **Créer une interaction tour par tour claire et intuitive**.
- **Gérer l'état du jeu et détecter la fin d'une partie**.

---

## **Règles du jeu**

### **Déroulement d’une partie**

1. Le joueur place ses bateaux sur une grille de jeu.
2. L'adversaire virtuel place également ses bateaux aléatoirement.
3. Le joueur et l'adversaire tirent à tour de rôle en essayant de deviner les positions des bateaux adverses.
4. Chaque tir est indiqué comme **touché** ou **manqué**.
5. L'objectif est de couler tous les bateaux adverses en premier.

### **Calcul du score**

- **Score basé sur le nombre total de tirs effectués** : Moins il y a de tirs, meilleur est le score.

---

## **Fonctionnalités du jeu**

- Placement manuel ou automatique des bateaux sur la grille.
- Tir alterné joueur/adversaire avec gestion des résultats (touché/coulé/manqué).
- Affichage clair et mis à jour de la grille de jeu après chaque tour.
- Gestion automatique des tirs de l'adversaire virtuel.
- Détection de la fin du jeu lorsque tous les bateaux sont coulés.
- Affichage du score final.

---

## **Exemples d’utilisation**

### **Scénario 1 – Début d’une partie**

```
Bienvenue dans Battle Ship Royale Solo !

Placez vos bateaux sur la grille pour commencer.
Grille actuelle :

  0 1 2 3 4
0 ~ ~ ~ ~ ~
1 ~ ~ ~ ~ ~
2 ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~
4 ~ ~ ~ ~ ~

Entrez la position initiale de votre bateau (format ligne,colonne) : 1,1
```

---

### **Scénario 2 – Tir et résultat**

```
À votre tour de tirer !
Grille actuelle des tirs :

  0 1 2 3 4
0 X ~ ~ ~ ~
1 ~ O ~ ~ ~
2 ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~
4 ~ ~ ~ ~ ~

Entrez la position du tir (ligne,colonne) : 0,1

Résultat : Touché !
```

---

### **Scénario 3 – Coulé un bateau adverse**

```
Entrez la position du tir (ligne,colonne) : 0,2

Résultat : Coulé ! Vous avez coulé un bateau adverse !
```

---

### **Scénario 4 – Fin du jeu**

```
Félicitations, vous avez gagné !

Score final :
- Nombre total de tirs : 15
- Bateaux adverses coulés : 3/3
```

---

## **Organisation des fichiers**

📂 `Phase_1_Fondamentaux/`

```
│── Phase_1_Consignes.md     # Instructions détaillées
│── battleship_initial.py    # Code de base à compléter
│── test_battleship.py       # Tests unitaires pour valider le jeu
```

---

## **Livrables attendus**

📌 **Code source final** de `battleship_initial.py`  
📌 **Documentation du code** sous forme de commentaires  
📌 **Un rapport expliquant :**

- L’architecture du programme.
- Les choix techniques effectués.
- Les difficultés rencontrées et solutions apportées.

---

## **Conseils pour réussir**

- **Testez votre code régulièrement**.
- **Développez progressivement** : commencez par les fonctions de base avant d’ajouter des complexités.
- **Utilisez des affichages (`print()`) pour faciliter le débogage**.
- **Commentez clairement votre code** pour en faciliter la compréhension.
- **Anticipez et gérez les cas d'erreurs** possibles (entrées utilisateur incorrectes, vérifications de conditions de fin de jeu, etc.).

---