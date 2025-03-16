# **Mini-Projet de Validation – "Défi du Mot Mystère"**

## **Contexte**

Ce projet consiste à développer un jeu où le joueur doit **deviner un maximum de mots dans un temps limité** (exemple : **2 minutes**).

- Le joueur peut proposer **une lettre à la fois** pour découvrir progressivement le mot.
- **S’il pense connaître le mot**, il peut tenter de l’écrire en entier.
- **Une mauvaise proposition de mot entraîne une pénalité de temps**.
- **À chaque mot trouvé, un nouveau mot est généré immédiatement**.
- **Le score final est basé sur le nombre de mots trouvés et les erreurs commises**.

Ce projet doit être réalisé **en autonomie** en complétant le code fourni.

[Voir les consignes détaillées](Phase_1_Fondamentaux/Phase_1_Consignes.md)

---

## **Objectifs pédagogiques**

- **Manipuler les structures de données** : listes, dictionnaires, fichiers texte.  
- **Utiliser les boucles et conditions pour créer un jeu interactif**.  
- **Gérer un fichier de mots et sélectionner aléatoirement un mot**.  
- **Créer une interaction en temps réel avec gestion d’un chronomètre**.  
- **Gérer une pénalité sur une mauvaise réponse**.

---

## **Règles du jeu**

### **Déroulement d’une partie**

1. Un **mot mystère est choisi aléatoirement** depuis un fichier contenant **1000 mots**.
2. Le joueur peut :
   - Proposer une **lettre** pour voir si elle est dans le mot.
   - **Taper un mot entier** s’il pense avoir deviné.
   - **S’il se trompe sur un mot entier, une pénalité de 5 secondes est appliquée**.
3. Une fois le mot trouvé, **un autre mot apparaît immédiatement**.
4. **L’objectif est de trouver le plus de mots possible avant la fin du temps imparti**.

### **Calcul du score**

- **+1 point** par mot trouvé.
- **-5 secondes** si le joueur propose un mot incorrect.
- **Affichage du score final à la fin du temps**.

---

## **Fonctionnalités du jeu**

- Sélectionner **aléatoirement un mot** depuis un fichier de **1000 mots** (`mots.txt`).
- **Afficher le mot partiellement masqué** (`M _ T _ U R E`).
- **Permettre au joueur de proposer des lettres ou un mot entier**.
- **Gérer les mauvaises propositions avec des pénalités de temps**.
- **Gérer un chronomètre en temps réel** (exemple : **2 minutes**).
- **Générer un nouveau mot dès qu’un mot est trouvé**.
- **Afficher le score final et le nombre de mots trouvés**.

---

## **Exemples d’utilisation**

### **Scénario 1 – Début d’une partie**

```
Bienvenue dans le Défi du Mot Mystère !

Objectif : Devinez un maximum de mots en 120 secondes.
Vous pouvez entrer une lettre OU deviner le mot entier.
Attention : Une mauvaise réponse sur un mot entier entraîne une pénalité de -5 secondes.

Un mot mystère a été choisi...
Mot actuel : _ _ _ _ _ _ _
Temps restant : 120s
Entrez une lettre ou un mot : T
```

---

### **Scénario 2 – Révélation progressive du mot**

```
Mot actuel : _ _ T _ _ _
Temps restant : 110s
Lettres essayées : T
Entrez une lettre ou un mot : A

Bonne réponse !
Mot actuel : _ A T _ _ _
Temps restant : 108s
Entrez une lettre ou un mot : X

Mauvaise réponse !
Mot actuel : _ A T _ _ _
Lettres essayées : T, A, X
Erreurs : 1
Temps restant : 105s
```

---

### **Scénario 3 – Deviner un mot entier**

```
Mot actuel : M A T _ _ _
Temps restant : 95s
Entrez une lettre ou un mot : MATURE

Bravo ! Vous avez trouvé le mot "MATURE" !
+1 point
Nouveau mot généré...
Mot actuel : _ _ _ _ _
Temps restant : 94s
```

---

### **Scénario 4 – Mauvaise réponse avec pénalité**

```
Mot actuel : B _ _ _ _ _
Temps restant : 50s
Entrez une lettre ou un mot : BOUTONNER

Mauvaise réponse !
Pénalité de -5s !
Temps restant : 45s
```

---

### **Scénario 5 – Fin du jeu**

```
Temps écoulé !

Score final :
- Mots trouvés : 7
- Mots ratés : 2
- Pénalités de temps : -10 secondes
```

---

## **Organisation des fichiers**

📂 `Phase_1_Fondamentaux/`

```
│── Phase_1_Consignes.md    # Instructions détaillées
│── mots.txt                # Fichier contenant 1000 mots
│── defi_mot_initial.py      # Code de base à compléter
│── test_defi_mot.py         # Tests unitaires pour valider le jeu
```

### **Fichier `mots.txt`**

- Contient **1000 mots aléatoires** (exemples : "MAISON", "ORDINATEUR", "PYTHON", "CERVEAU"…).
- Chaque mot doit être **en majuscules et sans accents** pour simplifier la gestion.

---

## **Livrables attendus**

📌 **Code source final** de `defi_mot_initial.py`  
📌 **Documentation du code** sous forme de commentaires  
📌 **Un rapport expliquant :**

- L’architecture du programme (comment vous avez structuré votre code).
- Les choix techniques effectués.
- Les difficultés rencontrées et les solutions trouvées.

---

## **Conseils pour réussir**

- **Testez régulièrement votre code** : Ne développez pas tout d’un coup sans vérifier son bon fonctionnement.
- **Commencez par des fonctionnalités simples**, puis ajoutez les optimisations.
- **Utilisez des affichages (`print()`) pour déboguer** et voir où ça bloque.
- **Commentez votre code** pour faciliter sa compréhension.
- **Anticipez les erreurs possibles** (mauvaises entrées utilisateur, fin du temps imparti, etc.).

---

**Bonne programmation !**
