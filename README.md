# **Défi du Mot Mystère - Guide de Développement**

## **Introduction**

Ce projet vise à développer un **jeu de devinette de mots** en trois phases progressives. Vous commencerez par une **version solo**, puis vous ajouterez un **mode multijoueur**, et enfin vous implémenterez une **intelligence artificielle** capable de jouer seule.

Chaque phase introduit des concepts essentiels en **Python**, **programmation réseau (sockets)** et **intelligence artificielle appliquée aux jeux**.

---

## **📄 Planning du Projet - Défi du Mot Mystère (1 Semaine)**  

| Jour | Matin (8h30 - 12h30) | Après-midi (13h30 - 17h30) | Début et fin des Phases |
|------|----------------------|---------------------------|---------------------------|
| **Lundi** | 🎯 **Présentation du projet** (Objectifs, organisation, livrables) <br> ⚙️ **Mise en place de l’environnement (Git, venv)** <br> 🔹 **[Cours POO](Utils/01-POO/README.md)** | 📝 **[Exercices POO](Utils/01-POO/exercices/)** <br> 🛠 **Implémentation du jeu solo (gestion des mots, affichage, chrono)** <br> ✅ **Finalisation et tests du mode solo** | **Phase 1 : Début et Fin** |
| **Mardi** | 🔹 **[Cours Réseau](Utils/02-Programmation_Reseau/README.md)** <br> 🖧 **[Exercice Client-Serveur](Utils/02-Programmation_Reseau/exercices/)** | 🛠 **Développement multijoueur** (Serveur + Clients) <br> 🔄 **Test du serveur et des connexions** | **Phase 2 : Début** |
| **Mercredi** | 🔗 **Gestion des connexions multiples** <br> 🛠 **Débogage et amélioration multijoueur** | ✅ **[Tests unitaires avec PyTest](Utils/03-PyTest/README.md)** <br> 🛠 **Validation du mode multijoueur** <br> 🔍 **Corrections finales** | **Phase 2 : Fin** |
| **Jeudi** | ✅ **Validation complète du projet** <br> 🤖 **Début du développement IA (Fréquences des lettres, analyse des mots possibles)** | *(Pas de cours l’après-midi)* | **Phase 3 : Début** |
| **Vendredi** | 🛠 **Optimisation et tests IA** <br> 📊 **Analyse et ajustements** | 🏆 **Concours IA : Matchs et comparaison des stratégies** | **Phase 3 : Fin** |

---

## **1. Résumé des Phases du Projet**

Le projet est divisé en trois phases. Vous devez les réaliser dans l’ordre en complétant le code fourni dans chaque dossier.

| Phase | Objectif | Lien vers les consignes |
|-------|---------|------------------------|
| **Phase 1 : Version Solo** | Implémenter un jeu où un joueur tente de deviner des mots en un temps limité. | [Consignes Phase 1](Phase_1_Fondamentaux/Phase_1_Consignes.md) |
| **Phase 2 : Mode Multijoueur** | Modifier le jeu pour permettre à plusieurs joueurs de jouer en réseau via un serveur. | [Consignes Phase 2](Phase_2_Multijoueurs/Phase_2_Consignes.md) |
| **Phase 3 : Intelligence Artificielle** | Développer un joueur virtuel capable de deviner les mots avec des stratégies avancées. | [Consignes Phase 3](Phase_3_IA/Phase_3_Consignes.md) |

Vous devez suivre ces étapes dans l’ordre et implémenter progressivement les fonctionnalités demandées.

---

## **2. Organisation du Projet**

Le projet est structuré comme suit :

```text
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

---

## **3. Utilisation d'un Environnement Virtuel**

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

## **4. Outils pour la Gestion du Projet en Solo**

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

## **5. Livrables à Rendre**

Tout au long du projet, plusieurs livrables peuvent être demandés pour évaluer votre travail.

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

## **7. Ressources**

Voici quelques liens utiles pour vous aider dans la réalisation du projet.

### **Documentation Python**

- [Documentation officielle de Python](https://docs.python.org/3/)
- [Tutoriel sur les fichiers en Python](https://realpython.com/read-write-files-python/)

### **Programmation Réseau**

- [Introduction aux sockets en Python](https://realpython.com/python-sockets/)
- [Exemples de serveurs et clients avec `socket`](https://docs.python.org/3/library/socket.html)

### **Tests et Débogage**

- [Documentation de `pytest`](https://docs.pytest.org/en/stable/)
- [Guide de débogage en Python](https://realpython.com/python-debugging-pdb/)

### **Intelligence Artificielle et Algorithmes**

- [Utilisation de statistiques pour améliorer une IA](https://towardsdatascience.com/basic-statistics-for-ai-enthusiasts-73ca91d3649a)
- [Concepts de base des heuristiques en IA](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-heuristic-search/)

### **Gestion de Projet**

- [Trello - Outil de gestion de tâches](https://trello.com/)
- [Notion - Outil de documentation et d'organisation](https://www.notion.so/)

---

## **8. Objectifs à Atteindre**

- **Phase 1** : Un jeu **fonctionnel en solo** avec gestion du temps et du score.
- **Phase 2** : Un **mode multijoueur stable**, où les joueurs peuvent proposer des lettres et voir l’évolution du mot en temps réel.
- **Phase 3** : Une **intelligence artificielle capable de jouer seule**, avec une logique d’apprentissage et d’optimisation.

L’objectif est d’avoir un projet **fonctionnel et bien structuré**, en appliquant de bonnes pratiques de développement.

Bonne programmation !
