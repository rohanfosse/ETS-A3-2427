# 🌐 **Projet Avancé – Battle Ship Royale Multijoueur 🎮**

📁 Fichiers : `serveur_battleship.py`, `client_battleship.py`  
📄 Consignes : `Phase_2_Consignes.pdf`

---

## 🌍 **Contexte**

Après avoir développé la version solo de **Battle Ship Royale**, vous passez désormais à la vitesse supérieure en ajoutant un mode multijoueur réseau. Plusieurs joueurs pourront désormais s'affronter en temps réel, chacun gérant sa propre grille et essayant de couler les bateaux adverses en premier.

---

## **Nouveautés et Objectifs pédagogiques**

### Nouveautés

- Implémentation d'un mode multijoueur en réseau compétitif.
- Gestion d'un serveur central coordonnant les parties et les échanges entre joueurs.
- Utilisation des sockets (`socket` module) pour la communication réseau.
- Synchronisation des états du jeu entre plusieurs joueurs en temps réel.

### Objectifs pédagogiques

✅ Comprendre et utiliser les sockets pour créer une application réseau.  
✅ Implémenter un modèle client-serveur efficace en Python.  
✅ Gérer la synchronisation et la cohérence des données entre plusieurs joueurs.  
✅ Adapter un projet existant pour intégrer des fonctionnalités avancées.  
✅ Renforcer les compétences en structuration du code et gestion des erreurs réseau.

---

## **Fonctionnalités principales**

### Mode de jeu multijoueur

- Chaque joueur possède sa propre grille avec ses bateaux.
- Les joueurs s'affrontent en temps réel, chaque tir envoyé au serveur est traité immédiatement.
- Le serveur central coordonne les tirs et communique les résultats (touché, manqué, coulé) à tous les joueurs concernés.
- La partie s'arrête dès qu'un joueur perd tous ses bateaux.

---

### Communication réseau

- Le serveur central (`serveur_battleship.py`) :
  - Gère les connexions et parties.
  - Maintient l’état global de chaque grille de jeu.
  - Diffuse les résultats des tirs aux joueurs concernés.

- Les clients joueurs (`client_battleship.py`) :
  - Se connectent au serveur et envoient leurs tirs.
  - Reçoivent les résultats des tirs adverses.
  - Affichent l'état actuel de leur grille et des grilles adverses (partiellement masquées).

---

### Gestion des sockets

**Serveur (`serveur_battleship.py`) :**

- Accepte et gère les connexions simultanées des joueurs.
- Gère l'état global des grilles et des bateaux.
- Envoie des mises à jour en temps réel sur l'état du jeu aux clients.

**Client (`client_battleship.py`) :**

- Se connecte au serveur pour rejoindre une partie.
- Envoie des commandes de tir.
- Affiche les mises à jour du serveur en temps réel.

---

## **Scénarios d’utilisation**

### **Exemple – Début d'une partie multijoueur**

#### Joueur A (Client 1)

```
Connexion au serveur établie.
Placez vos bateaux sur la grille.
Attente des autres joueurs...
```

#### Joueur B (Client 2)

```
Connexion au serveur établie.
Placez vos bateaux sur la grille.
Attente des autres joueurs...
```

#### Serveur

```
Tous les joueurs connectés. Début de la partie !
Tour du Joueur A.
```

### **Exemple – Tir et résultat**

#### Joueur A

```
Votre tour de tirer.
Entrez les coordonnées (ligne,colonne) : 2,3
Résultat : Touché !
```

#### Joueur B

```
Le joueur A a tiré sur (2,3).
Résultat : Votre bateau a été touché !
```

---

## **Organisation des fichiers**

📂 `Phase_2_Multijoueur/`

```
│── 📄 Phase_2_Consignes.pdf       # Instructions détaillées
│── serveur_battleship.py          # Serveur du jeu
│── client_battleship.py           # Client joueur
│── test_multijoueur.py            # Tests unitaires pour valider le multijoueur
│── utils.py                       # Fonctions utilitaires partagées
```

---

## **Suggestions techniques**

### Modules recommandés

- `socket` pour la communication réseau.
- `threading` pour gérer plusieurs joueurs simultanément.

### Gestion des données

Utilisez une structure claire pour maintenir l'état global du jeu sur le serveur, par exemple :

```python
etat_jeu = {
    "joueurA": {"grille": [...], "bateaux_restants": 3},
    "joueurB": {"grille": [...], "bateaux_restants": 2},
}
```

- Synchronisez cet état avec tous les joueurs via des messages JSON envoyés sur les sockets (`json.dumps()` / `json.loads()`).

---

## **Conseils pour réussir**

- **Développez progressivement** : commencez par une connexion simple, puis ajoutez des interactions plus complexes.
- **Testez en local** avant de déployer en réseau.
- **Utilisez des logs (`print`)** côté serveur pour faciliter le débogage.
- **Anticipez les erreurs réseau** : gérez les déconnexions imprévues, les erreurs de communication, etc.

---

**Bonne programmation !**