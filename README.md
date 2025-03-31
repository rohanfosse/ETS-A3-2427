# 🚢 **Battle Ship Royale - Guide de Développement en Binôme**

## **Introduction**

Ce projet a pour objectif de développer, **en binôme**, un **jeu de bataille navale interactif** en trois phases progressives. Vous commencerez par une **version solo**, poursuivrez avec un **mode multijoueur**, et terminerez par l’implémentation d’une **intelligence artificielle** capable de jouer seule.

Chaque phase introduit des notions clés en **Python**, **programmation réseau (sockets)** et **intelligence artificielle appliquée aux jeux**.

---

## **📄 Planning du Projet - Battle Ship Royale (1 Semaine)**  

| Jour | Matin (8h30 - 12h30) | Après-midi (13h30 - 17h30) | Début et fin des Phases |
|------|----------------------|---------------------------|---------------------------|
| **Lundi** | 🎯 **Présentation du projet** (Objectifs, organisation, livrables) <br> ⚙️ **Installation de l’environnement de développement (Git, venv)** <br> 🔹 **[Cours Programmation Orientée Objet (POO)](Ressources_Utiles/01-POO/README.md)** | 📝 **[Exercices POO](Ressources_Utiles/01-POO/exercices/)** <br> 🛠 **Développement du jeu solo (grille, placement des bateaux, tirs)** <br> ✅ **Tests et validation du mode solo** | **Phase 1 : Début et Fin** |
| **Mardi** | 🔹 **[Cours Programmation Réseau](Ressources_Utiles/02-Programmation_Reseau/README.md)** <br> 🖧 **[Exercices Client-Serveur](Ressources_Utiles/02-Programmation_Reseau/exercices/)** | 🛠 **Implémentation du multijoueur réseau** (Serveur + Clients) <br> 🔄 **Validation du serveur et gestion des connexions** | **Phase 2 : Début** |
| **Mercredi** | 🔗 **Gestion avancée des connexions multiples** <br> 🛠 **Débogage et optimisation du mode multijoueur** | ✅ **[Tests unitaires avec PyTest](Ressources_Utiles/03-PyTest/README.md)** <br> 🛠 **Finalisation et tests approfondis** <br> 🔍 **Corrections et améliorations finales** | **Phase 2 : Fin** |
| **Jeudi** | ✅ **Validation intermédiaire du projet** <br> 🤖 **Introduction à l’Intelligence Artificielle (stratégies et prédiction)** | *(Après-midi libre)* | **Phase 3 : Début** |
| **Vendredi** | 🛠 **Développement et amélioration IA** <br> 📊 **Tests, optimisation et analyse des résultats** | 🏆 **Tournoi IA : Évaluation et comparaison des stratégies** | **Phase 3 : Fin** |

---

## **1. Résumé des Phases du Projet**

Le projet se déroule en trois phases progressives à réaliser dans l’ordre, **en collaboration à deux**.

| Phase | Objectif | Lien vers les consignes |
|-------|---------|------------------------|
| **Phase 1 : Version Solo** | Jeu solo avec un adversaire virtuel simple. | [Consignes Phase 1](Phase_1_Fondamentaux/Phase_1_Consignes.md) |
| **Phase 2 : Mode Multijoueur** | Ajout du multijoueur réseau avec gestion simultanée des joueurs. | [Consignes Phase 2](02-Jeu_Multijoueur/Phase_2_Consignes.md) |
| **Phase 3 : Intelligence Artificielle** | Développement d’une IA capable de jouer efficacement et d'apprendre des stratégies de jeu. | [Consignes Phase 3](Phase_3_IA/Phase_3_Consignes.md) |

---

## **2. Organisation du Projet**

Le projet est structuré de la façon suivante :

```text
├── Phase_1_Fondamentaux
│   ├── Phase_1_Consignes.md
│   └── battleship_initial.py
├── Phase_2_Multijoueurs
│   ├── Phase_2_Consignes.md
│   ├── client_battleship.py
│   ├── serveur_battleship.py
│   └── test_multijoueur.py
├── Phase_3_IA
│   ├── Phase_3_Consignes.md
│   └── joueur_virtuel.py
└── README.md
```

Chaque binôme peut ajouter des fichiers ou dossiers pour structurer son code.

---

## **3. Environnement Virtuel Python**

Pour faciliter le travail en binôme et garantir une cohérence des dépendances :

```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows
```

Créer un fichier `requirements.txt` :

```bash
pip freeze > requirements.txt
```

Et l’installer sur une autre machine :

```bash
pip install -r requirements.txt
```

---

## **4. Outils Collaboratifs Conseillés en Binôme**

### **Gestion du Code**

- **GitHub / GitLab** (avec un repo partagé)
- Commits fréquents, clairs, avec une branche par fonctionnalité si besoin.

### **Organisation et Répartition des Tâches**

- **Notion / Trello** pour définir qui fait quoi
- **Journal de bord commun** (markdown, Google Doc…) pour consigner vos choix et obstacles

### **Débogage et Tests**

- Utilisation de `print()` pour le suivi
- Mise en place de **tests unitaires partagés** avec `pytest`

---

## **5.Livrables à Rendre**

Tout au long du projet, plusieurs livrables peuvent être demandés pour évaluer votre travail.

### **Phase 1 : Version Solo**
📌 **Code source final** de `battleship_initial.py`  
📌 **Documentation du code** sous forme de commentaires  
📌 **Un rapport (PDF ou Markdown) expliquant :**  
   - L’architecture du programme (comment vous avez structuré votre code).  
   - Les choix techniques effectués.  
   - Les difficultés rencontrées et les solutions trouvées.  

---

### **Phase 2 : Mode Multijoueur**
📌 **Code source final** de `serveur_battleship.py` et `client_battleship.py`  
📌 **Fichier `test_multijoueur.py` fonctionnel**  
📌 **Un rapport expliquant :**  
   - Comment fonctionne l'échange de données entre client et serveur.  
   - Les problèmes de synchronisation et comment ils ont été résolus.  
   - Les tests réalisés pour valider votre implémentation.  

---

### **Phase 3 : Intelligence Artificielle**
📌 **Code source final** de `joueur_virtuel.py`  
📌 **Un rapport expliquant :**  
   - Les stratégies utilisées pour l'IA (placement des bateaux, analyse des tirs précédents, prise de décision).  
   - Les performances de l'IA (taux de réussite, nombre moyen de tirs pour couler un adversaire).  
   - Une comparaison avec un joueur humain (si possible).
   - 
---

## **6. Conseils pour Travailler Efficacement en Binôme**

- **Communiquez souvent** sur l’état d’avancement
- **Divisez clairement les tâches**, mais **relisez le travail de l’autre**
- **Gardez un repo à jour et synchronisé**
- **Testez chaque ajout de code**
- **Planifiez des points réguliers** pour vérifier que tout avance

---

## **7. Ressources Utiles**

### Python & Réseau

- [Docs Python](https://docs.python.org/3/)
- [Sockets Python](https://realpython.com/python-sockets/)

### Outils & Gestion

- [GitHub](https://github.com/)
- [Trello](https://trello.com/)
- [Notion](https://www.notion.so/)

### Débogage & IA

- [Guide `pytest`](https://docs.pytest.org/en/stable/)
- [Debugging en Python](https://realpython.com/python-debugging-pdb/)
- [Heuristiques IA](https://en.wikipedia.org/wiki/Heuristic_(computer_science))
  
---

## **8. Objectifs Final par Binôme**

- 🎯 **Phase 1** : Jeu solo complet
- 🎯 **Phase 2** : Multijoueur fonctionnel et stable
- 🎯 **Phase 3** : IA stratégique et performante

Le projet doit être **propre, testé, structuré, et collaboratif**.

Bonne programmation à tous les binômes ! 👥💻🚢
