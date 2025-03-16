# **📜 Cahier des Charges – Projet Python : "CryptoBench – Analyse et Comparaison des Algorithmes de Chiffrement"** 🔐

---

## **🌍 Contexte : Évaluation et Optimisation des Algorithmes de Cryptographie**

La cryptographie est un élément fondamental de la sécurité informatique. Toutefois, tous les algorithmes ne se valent pas : certains sont rapides mais peu sécurisés, d’autres sont robustes mais très gourmands en ressources.

L’objectif de ce projet est de **comparer et analyser différents algorithmes de chiffrement et de déchiffrement** en mesurant leurs performances en **temps d’exécution, consommation mémoire et complexité algorithmique**.

À travers ce projet, les étudiants devront **implémenter, tester et comparer plusieurs méthodes de chiffrement et de déchiffrement**, comprendre leurs **forces et faiblesses** et explorer leurs **applications pratiques**.

---

## **1️⃣ Objectifs pédagogiques**

✅ **Implémentation de plusieurs algorithmes de chiffrement et déchiffrement**.  
✅ **Analyse des performances et de la complexité algorithmique** (`O(n)`, `O(n³)`, etc.).  
✅ **Visualisation des résultats sous forme de graphiques**.  
✅ **Comprendre les différences entre chiffrement symétrique et asymétrique**.  
✅ **Réalisation d’attaques pour tester la robustesse des algorithmes**.

---

## **2️⃣ Fonctionnalités attendues**

### **A. Algorithmes de cryptographie à implémenter**

📌 **Chiffrement symétrique**

- **Chiffrement de César** (simple substitution, vulnérable aux attaques par fréquence).
- **Chiffrement XOR** (opération bit à bit, souvent utilisé dans les flux).
- **AES (Advanced Encryption Standard)** (bloc de 128 bits, très sécurisé).

📌 **Chiffrement asymétrique**

- **RSA (Rivest-Shamir-Adleman)** (basé sur la factorisation des grands nombres premiers).

📌 **Fonctions de hachage**

- **SHA-256** (hachage sécurisé).
- **MD5** (hachage rapide mais faible en sécurité).

---

### **B. Déchiffrement des algorithmes**

Les étudiants devront également **implémenter le déchiffrement** des méthodes suivantes :

1️⃣ **Chiffrement de César**

- Déchiffrer un message en **inversant le décalage**.
- Tester une **attaque par brute-force** (essai des 25 clés possibles).

2️⃣ **Chiffrement XOR**

- Déchiffrer un texte en appliquant **la même clé XOR utilisée au départ**.
- Vérifier la résistance en analysant la **fréquence des caractères**.

3️⃣ **AES**

- Déchiffrer un texte en **mode ECB** (Electronic Code Book).
- Comprendre pourquoi **ce mode est vulnérable** et proposer des alternatives.

4️⃣ **RSA**

- Générer une **paire de clés publique/privée**.
- Chiffrer et déchiffrer un message à l’aide des clés générées.

---

### **C. Analyse et Comparaison des Algorithmes**

📌 **Expériences à réaliser :**  
✅ **Mesurer le temps d’exécution des algorithmes** pour différentes tailles de fichiers.  
✅ **Analyser la consommation mémoire** pour chaque méthode.  
✅ **Comparer les complexités théoriques et les résultats expérimentaux**.  
✅ **Visualiser les performances sous forme de graphes**.

📌 **Outils à utiliser :**

- **`timeit`** pour mesurer le temps d’exécution.
- **`memory_profiler`** pour évaluer la consommation mémoire.
- **`matplotlib`** pour générer des graphiques.

---

## **3️⃣ Expérimentation et Tests**

### **A. Jeux de tests**

📌 **Les étudiants devront chiffrer et déchiffrer** :  
✅ Un texte court (10 caractères).  
✅ Un texte long (500 000 caractères).  
✅ Un fichier binaire (image, PDF).

### **B. Attaques sur les algorithmes**

📌 **Les étudiants devront tester** :  
✅ Une **attaque brute-force** sur César et XOR.  
✅ Une **analyse fréquentielle** pour casser un message chiffré.  
✅ Une **tentative de factorisation de clé RSA** (simulation avec petits nombres).

---

## **4️⃣ Contraintes Techniques et Optimisation**

📌 **Langages et bibliothèques**  
✅ **Python 3.x**  
✅ **`pycryptodome`** pour AES et RSA.  
✅ **`hashlib`** pour SHA-256 et MD5.  
✅ **`matplotlib`, `numpy`** pour la visualisation des performances.

📌 **Optimisation des tests**  
✅ Exécuter chaque algorithme **sur plusieurs tailles de données**.  
✅ Réduire les **temps d’exécution** en utilisant des méthodes optimisées.

---

## **5️⃣ Déroulement du projet (4 jours et demi)**

📌 **Jour 1 : Implémentation des algorithmes de chiffrement**

- Implémentation de **César, XOR, AES, RSA, SHA-256, MD5**.
- Vérification du bon fonctionnement.

📌 **Jour 2 : Déchiffrement et tests de robustesse**

- Implémentation du **déchiffrement pour chaque méthode**.
- Test des **attaques sur les algorithmes faibles**.

📌 **Jour 3 : Mesures de performance et visualisation**

- Collecte des **temps d’exécution** pour différents jeux de données.
- Génération des **courbes de performance** et comparaison.

📌 **Jour 4 (Matin) : Optimisation et étude de cas**

- Comparaison entre **chiffrement symétrique et asymétrique**.
- Discussion sur **le choix des algorithmes selon les contextes**.

📌 **Jour 5 : Présentation et synthèse**

- **Présentation des conclusions et des choix d’algorithmes optimaux**.
- **Démonstration des performances et des attaques testées**.

---

## **6️⃣ Livrables attendus**

✔️ **Code source bien structuré et documenté**.  
✔️ **Résultats des mesures de performance sur différents jeux de données**.  
✔️ **Graphiques comparant les temps d’exécution et la consommation mémoire**.  
✔️ **Rapport final expliquant les différences théoriques et expérimentales**.  
✔️ **Présentation des conclusions et recommandations**.

---

## **7️⃣ Critères d’évaluation**

📌 **Qualité du code et modularité** (20%)  
📌 **Exactitude des implémentations des algorithmes** (25%)  
📌 **Pertinence et rigueur des mesures expérimentales** (20%)  
📌 **Visualisation et analyse des résultats** (15%)  
📌 **Présentation et rapport final** (10%)  
📌 **Optimisation et réflexion sur les choix d’algorithmes** (10%)

---

## **8️⃣ Conclusion**

Ce projet permet aux étudiants de **comprendre en profondeur les algorithmes de cryptographie**, **évaluer leurs performances**, **tester leur robustesse** et **choisir le bon chiffrement en fonction du contexte**.

En expérimentant avec des **attaques et des mesures de performance**, les étudiants acquerront **une vision critique et analytique** de la cryptographie appliquée.

🔐 **Prêts à analyser et optimiser la sécurité des algorithmes ?** 🚀
