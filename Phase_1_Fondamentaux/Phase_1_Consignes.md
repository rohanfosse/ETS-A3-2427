# **📜 Mini-Projet de Validation – "Défi du Mot Mystère"** ⏳🔠

📁 **Fichier : `mini_projet_defi_mot.py`**  
📄 **Fichier : `Phase_1_Consignes.pdf`**

---

## **🌍 Contexte**

Le joueur doit **deviner le plus de mots possible dans un temps imparti** (ex: **2 minutes**).

- Il propose **une lettre à la fois** pour révéler progressivement le mot.
- **S’il pense connaître le mot**, il peut tenter de l’écrire en entier.
- **S’il se trompe sur le mot entier**, une **pénalité** est appliquée.
- **À chaque mot trouvé, un nouveau mot est généré immédiatement**.
- **Le score final est basé sur le nombre de mots trouvés** et le **nombre d’erreurs**.

---

## **1️⃣ Objectifs pédagogiques**

✅ **Manipuler les structures de données** : listes, dictionnaires, fichiers texte.  
✅ **Utiliser les boucles et conditions pour créer un jeu dynamique**.  
✅ **Gérer un fichier de mots et sélectionner aléatoirement un mot**.  
✅ **Créer une interaction en temps réel avec gestion du chrono**.  
✅ **Gérer la pénalité sur une mauvaise réponse**.

---

## **2️⃣ Règles du jeu**

📌 **Déroulement d’une partie** :  
1️⃣ Un mot mystère est **choisi aléatoirement** depuis un fichier contenant **1000 mots**.  
2️⃣ Le joueur peut :

- Proposer une **lettre** pour voir si elle est dans le mot.
- **Taper directement un mot entier** s’il pense avoir deviné.
- **S’il se trompe sur un mot entier, il a une pénalité de 5 secondes**.  
  3️⃣ **Une fois le mot trouvé, un autre mot apparaît immédiatement**.  
  4️⃣ **Le but est de trouver le plus de mots possible avant la fin du temps**.

📌 **Calcul du score** :  
✅ **+1 point** par mot trouvé.  
❌ **-5 secondes** si le joueur propose un mot incorrect.  
✅ **Affichage du score final à la fin du temps imparti**.

---

## **3️⃣ Fonctionnalités du jeu**

✅ **Sélectionner aléatoirement un mot depuis un fichier de 1000 mots (`mots.txt`)**.  
✅ **Afficher le mot masqué partiellement** (`M _ T _ U R E`).  
✅ **Permettre au joueur de proposer des lettres ou un mot entier**.  
✅ **Gérer les mauvaises propositions avec pénalités de temps**.  
✅ **Gérer un chrono en temps réel (ex: 2 minutes)**.  
✅ **Générer un nouveau mot dès qu’un mot est trouvé**.  
✅ **Affichage du score final et du nombre de mots trouvés**.

---

## **4️⃣ Exemples d’utilisation**

### **📌 Scénario 1 – Début d’une partie**

```
🎮 Bienvenue dans le Défi du Mot Mystère ! ⏳

📌 Objectif : Devinez un maximum de mots en **120 secondes**.
📌 Vous pouvez entrer une lettre OU deviner le mot entier.
📌 ⚠️ Mauvaise réponse sur un mot entier = -5 secondes !

Un mot mystère a été choisi...
Mot actuel : _ _ _ _ _ _ _
Temps restant : 120s
Entrez une lettre ou un mot : **T**
```

---

### **📌 Scénario 2 – Révélation progressive du mot**

```
Mot actuel : _ _ T _ _ _
Temps restant : 110s
Lettres essayées : T
Entrez une lettre ou un mot : **A**

Bonne réponse ! 🎉
Mot actuel : _ A T _ _ _
Temps restant : 108s
Entrez une lettre ou un mot : **X**

Mauvaise réponse ❌
Mot actuel : _ A T _ _ _
Lettres essayées : T, A, X
Erreurs : 1
Temps restant : 105s
```

---

### **📌 Scénario 3 – Deviner un mot entier**

```
Mot actuel : M A T _ _ _
Temps restant : 95s
Entrez une lettre ou un mot : **MATURE**

🎉 Bravo ! Vous avez trouvé le mot "MATURE" !
✅ +1 point
🔄 Nouveau mot généré...
Mot actuel : _ _ _ _ _
Temps restant : 94s
```

---

### **📌 Scénario 4 – Mauvaise réponse avec pénalité**

```
Mot actuel : B _ _ _ _ _
Temps restant : 50s
Entrez une lettre ou un mot : **BOUTONNER**

❌ Mauvaise réponse !
⏳ Pénalité de -5s !
Temps restant : 45s
```

---

### **📌 Scénario 5 – Fin du jeu**

```
⏳ Temps écoulé ! 🎉

🏆 Score final :
- Mots trouvés : **7**
- Mots ratés : **2**
- Pénalités de temps : **-10 secondes**
```

---

## **📂 Organisation des fichiers**

📂 `Phase_1_Fondamentaux/`

```
│── 📄 Phase_1_Consignes.pdf        # Instructions détaillées
│── 📄 mots.txt                     # Fichier contenant 1000 mots
│── defi_mot_initial.py         # Fichier principal du jeu
│── test_defi_mot.py                # Tests unitaires pour valider le jeu
```

📌 **Fichier `mots.txt`**

- Contient **1000 mots aléatoires** (ex: "MAISON", "ORDINATEUR", "PYTHON", "CERVEAU"…).
- Chaque mot doit être **en majuscules et sans accents** pour simplifier la gestion.

---
