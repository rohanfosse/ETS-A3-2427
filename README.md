# **Défi du Mot Mystère - Guide de Développement**

## **Introduction**

Ce projet vise à développer un **jeu de devinette de mots**, en trois phases progressives. Vous commencerez par une **version solo**, puis vous ajouterez un **mode multijoueur**, et enfin vous implémenterez une **intelligence artificielle** capable de jouer seule.

Chaque phase du projet introduit des concepts essentiels en **Python**, **programmation réseau (sockets)** et **intelligence artificielle appliquée aux jeux**.

---

## **1. Organisation du Projet**

Le projet est structuré en trois phases, chacune avec un squelette de code à compléter :

```
├── Phase_1_Fondamentaux
│   ├── Phase_1_Consignes.md
│   └── defi_mot_initial.py
├── Phase_2_Multijoueurs
│   ├── Phase_2_Consignes.md
│   ├── client_defi_mot.py
│   ├── serveur_defi_mot.py
│   └── test_multijoueur.py
├── Phase_3_IA
│   ├── Phase_3_Consignes.md
│   └── joueur_virtuel.py
└── README.md
```

Chaque phase comprend :

- **Un fichier de consignes détaillé** (`Phase_X_Consignes.md`).
- **Un squelette de code** (`.py`) à compléter et enrichir.
- **D'éventuels fichiers de tests** (`test_*.py`).

Vous devez suivre ces phases dans l’ordre et implémenter progressivement les fonctionnalités demandées.

---

## **2. Utilisation d'un Environnement Virtuel**

L'utilisation d'un **environnement virtuel** est recommandée pour :

- **Isoler les dépendances du projet** afin d’éviter les conflits avec d’autres projets Python installés sur votre machine.
- **Assurer la reproductibilité** : un fichier `requirements.txt` permet d’installer exactement les mêmes versions de bibliothèques sur une autre machine.
- **Travailler sur plusieurs versions de Python** sans interférer avec les installations globales.

### **Création et activation de l’environnement**

```sh
python -m venv env
source env/bin/activate  # Sur macOS/Linux
env\Scripts\activate  # Sur Windows
```

### **Installation des dépendances**

Si des bibliothèques sont nécessaires, créez un fichier `requirements.txt` :

```sh
pip freeze > requirements.txt
```

Puis installez-les sur une autre machine avec :

```sh
pip install -r requirements.txt
```

---

## **3. Outils pour la Gestion du Projet en Solo**

Même si vous travaillez seul, il est important de bien organiser votre travail. Voici quelques outils utiles :

### **Gestion du Code**

- **GitHub / GitLab** : Versionner votre projet, sauvegarder vos évolutions et revenir à une version précédente en cas d’erreur.
- **Commit régulier** : Faire des commits à chaque fonctionnalité importante permet d'éviter de perdre son travail.
- **Utilisation des branches** (optionnel) : Travailler sur une fonctionnalité spécifique sans modifier directement le code principal.

### **Suivi du Développement**

- **Trello / Notion** : Organiser les tâches sous forme de tableau (To-Do, En cours, Terminé).
- **Journal de bord** : Prendre des notes sur les problèmes rencontrés et les solutions trouvées.

### **Débogage et Tests**

- **Logs (`print()`)** : Pour afficher l’évolution du programme et comprendre les erreurs.
- **Pytest** : Pour écrire des tests automatisés et valider que le code fonctionne après chaque modification.

---

## **4. Exécution et Tests**

### **Exécuter la version solo**

```sh
python Phase_1_Fondamentaux/defi_mot_initial.py
```

### **Lancer le mode multijoueur**

1. **Démarrer le serveur** :

   ```sh
   python Phase_2_Multijoueurs/serveur_defi_mot.py
   ```

2. **Démarrer un client** :

   ```sh
   python Phase_2_Multijoueurs/client_defi_mot.py
   ```

### **Tester le projet**

Des fichiers de tests unitaires sont fournis. Exécutez-les pour vérifier votre implémentation :

```sh
pytest Phase_2_Multijoueurs/test_multijoueur.py
```

---

## **5. Livrables à Rendre**

Tout au long du projet, plusieurs livrables peuvent être demandés pour évaluer votre travail :

### **Phase 1 : Version Solo**

📌 **Code source final** de `defi_mot_initial.py`  
📌 **Documentation du code** sous forme de commentaires  
📌 **Un rapport (PDF ou Markdown) expliquant :**

- L’architecture du programme (comment vous avez structuré votre code)
- Les choix techniques effectués
- Les difficultés rencontrées et les solutions trouvées

---

### **Phase 2 : Mode Multijoueur**

📌 **Code source final** de `serveur_defi_mot.py` et `client_defi_mot.py`  
📌 **Fichier `test_multijoueur.py` fonctionnel**  
📌 **Un rapport expliquant :**

- Comment fonctionne l'échange de données entre client et serveur
- Les problèmes de synchronisation et comment ils ont été résolus
- Les tests réalisés pour valider votre implémentation

---

### **Phase 3 : Intelligence Artificielle**

📌 **Code source final** de `joueur_virtuel.py`  
📌 **Un rapport expliquant :**

- Les stratégies utilisées pour l'IA (fréquence des lettres, filtrage des mots possibles, prise de décision)
- Les performances de l'IA (taux de réussite, temps moyen pour deviner un mot)
- Une comparaison avec un joueur humain (si possible)

---

## **6. Conseils pour Réussir**

- **Testez régulièrement votre code** : Ne développez pas tout d’un coup sans vérifier si ça fonctionne.
- **Commencez par des fonctionnalités simples** avant d'ajouter des optimisations.
- **Utilisez des prints et des logs** pour voir où ça bloque.
- **Ne négligez pas la documentation** : Expliciter vos choix facilitera la compréhension du projet.
- **Anticipez les erreurs possibles** (mauvaises entrées utilisateur, client qui se déconnecte, etc.).

---

## **7. Objectifs à Atteindre**

- **Phase 1** : Un jeu **fonctionnel en solo** avec gestion du temps et du score.
- **Phase 2** : Un **mode multijoueur stable**, où les joueurs peuvent proposer des lettres et voir l’évolution du mot en temps réel.
- **Phase 3** : Une **intelligence artificielle capable de jouer seule**, avec une logique d’apprentissage et d’optimisation.

L’objectif est d’avoir un projet **fonctionnel et bien structuré**, en appliquant de bonnes pratiques de développement.

Bonne programmation !
