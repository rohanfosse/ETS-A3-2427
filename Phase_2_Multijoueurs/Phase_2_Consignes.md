# 📜 Projet Avancé – "Défi du Mot Mystère Multijoueur" 🌐🎮

📁 Fichier : `defi_mot_multijoueur.py`  
📄 Fichier : `Phase_2_Consignes.pdf`

---

## 🌍 Contexte

Après avoir développé une version solo du jeu "Défi du Mot Mystère", il est temps de passer à la vitesse supérieure en ajoutant un mode multijoueur. Le jeu devient une expérience interactive où plusieurs joueurs peuvent s'affronter ou collaborer en temps réel grâce à l'utilisation des sockets pour gérer la communication réseau.

---

## 1️⃣ Nouveautés et Objectifs pédagogiques

### Nouveautés

- Implémentation d'un mode multijoueur en réseau (coopératif ou compétitif).
- Gestion d'un serveur central qui coordonne les joueurs.
- Utilisation des sockets (`socket` module) pour la communication entre le serveur et les clients.
- Synchronisation des états du jeu (mots, scores, chronomètre) entre plusieurs joueurs.

### Objectifs pédagogiques

✅ Comprendre et utiliser les sockets pour créer une application réseau.  
✅ Implémenter un modèle client-serveur simple en Python.  
✅ Gérer la synchronisation des données entre plusieurs instances du jeu.  
✅ Adapter un projet existant pour y intégrer des fonctionnalités avancées.  
✅ Renforcer les compétences en structuration de code et gestion d'erreurs réseau.

---

## 2️⃣ Fonctionnalités principales

### Modes de jeu multijoueur

1. Mode Coopératif :

   - Les joueurs travaillent ensemble pour deviner le plus de mots possible dans un temps imparti.
   - Les efforts sont combinés : chaque joueur peut proposer une lettre ou un mot entier.
   - Le score final est partagé.

2. Mode Compétitif :
   - Les joueurs s'affrontent pour trouver le plus de mots possible.
   - Le premier joueur à deviner correctement un mot gagne 1 point.
   - Les pénalités sont individuelles (-5 secondes sur le chrono personnel en cas d'erreur).

---

### Communication réseau

- Un serveur central gère les parties :
  - Il sélectionne les mots mystères et envoie l'état actuel du jeu à tous les joueurs.
  - Il reçoit les propositions des joueurs (lettres ou mots) et met à jour l'état du jeu.
- Les clients se connectent au serveur pour participer à une partie :
  - Chaque client affiche l'état actuel du mot mystère, le score et le temps restant.
  - Les actions des autres joueurs sont reflétées en temps réel.

---

### Gestion des sockets

1. Serveur (`serveur_defi_mot.py`) :

   - Gère les connexions des joueurs.
   - Maintient l'état global du jeu (mot mystère, scores, chronomètre).
   - Diffuse les mises à jour à tous les clients.

2. Client (`client_defi_mot.py`) :
   - Se connecte au serveur.
   - Affiche l'état actuel du jeu.
   - Envoie au serveur les propositions (lettres ou mots) faites par le joueur.

---

## 3️⃣ Scénarios d’utilisation

### 📌 Exemple 1 – Mode Coopératif

#### Joueur A (Client 1)

```
Mot actuel : _ _ _ _ _ _
Temps restant : 120s
Entrez une lettre ou un mot : T
```

#### Joueur B (Client 2)

```
Mot actuel : _ _ T _ _ _
Temps restant : 118s
Entrez une lettre ou un mot : A
```

#### Serveur

```
Lettre "T" trouvée par Joueur A !
Lettre "A" trouvée par Joueur B !
Mot actuel : _ A T _ _ _
Temps restant : 115s
```

---

### 📌 Exemple 2 – Mode Compétitif

#### Joueur A (Client 1)

```
Mot actuel : _ _ _ _ _
Temps restant : 90s
Entrez une lettre ou un mot : P

Bonne réponse ! 🎉
Mot actuel : P _ _ _ _
Temps restant : 88s
Score Joueur A : 1
Score Joueur B : 0
```

#### Joueur B (Client 2)

```
Mot actuel : P _ _ _ _
Temps restant : 88s
Entrez une lettre ou un mot : PYTHON

🎉 Bravo ! Vous avez trouvé le mot "PYTHON" !
Score Joueur A : 1
Score Joueur B : 1
```

---

## 4️⃣ Organisation des fichiers

📂 `Phase_2_Multijoueur/`

```
│── 📄 Phase_2_Consignes.pdf        # Instructions détaillées
│── 📄 mots.txt                     # Fichier contenant 1000 mots
│── serveur_defi_mot.py             # Serveur principal du jeu
│── client_defi_mot.py              # Client joueur
│── test_multijoueur.py             # Tests unitaires pour valider le mode multijoueur
│── utils.py                        # Fonctions utilitaires partagées entre client et serveur
```

---

## Suggestions techniques

### 📌 Modules recommandés

- `socket` pour la communication réseau.
- `threading` pour gérer plusieurs connexions simultanées sur le serveur.
- `time` pour synchroniser le chronomètre entre clients.

### 📌 Gestion des données

- Utiliser des structures comme des dictionnaires pour stocker l’état global du jeu sur le serveur :

```python
etat_jeu = {
    "mot_actuel": "_ A T _ _ _",
    "mots_trouves": [],
    "scores": {"JoueurA": 3, "JoueurB": 5},
    "temps_restant": 120,
}
```

- Synchroniser cet état avec tous les clients via des messages JSON envoyés sur les sockets (`json.dumps()` / `json.loads()`).

## Section optionnelle : Affichage graphique avec Pygame

Pour les étudiants qui terminent rapidement ou souhaitent aller plus loin, nous proposons d'ajouter une interface graphique au jeu en utilisant la bibliothèque Pygame. Cette extension permettra de visualiser le déroulement des parties de manière plus interactive et immersive.

### Objectifs

1. Créer une fenêtre graphique pour afficher l'état du jeu.
2. Représenter visuellement le mot mystère, les scores et le chronomètre.
3. Ajouter des animations simples pour les actions des joueurs.

### Étapes suggérées

#### 1. Installation et configuration de Pygame

- Installez Pygame via pip.
- Importez Pygame dans votre projet.

#### 2. Création de la fenêtre de jeu

- Initialisez une fenêtre Pygame avec une taille appropriée.
- Définissez un titre pour la fenêtre.

#### 3. Affichage des éléments du jeu

- Créez des fonctions pour afficher :
  - Le mot mystère partiellement révélé.
  - Les scores des joueurs.
  - Le temps restant.
- Utilisez des polices et des couleurs différentes pour chaque élément.

#### 4. Mise à jour de l'affichage

- Synchronisez l'affichage avec les mises à jour reçues du serveur.
- Rafraîchissez l'écran après chaque changement d'état.

#### 5. Gestion des événements

- Capturez les entrées clavier pour les propositions de lettres ou de mots.
- Gérez la fermeture de la fenêtre.

#### 6. Animations simples (bonus)

- Ajoutez des effets visuels simples pour les bonnes et mauvaises réponses.
- Animez le décompte du temps.

### Indices et conseils

- Utilisez `pygame.display.set_mode()` pour créer la fenêtre.
- Les fonctions `pygame.font.Font()` et `font.render()` sont utiles pour afficher du texte.
- La méthode `screen.blit()` permet de dessiner des éléments sur l'écran.
- Utilisez une boucle d'événements Pygame pour gérer les interactions utilisateur.
- Pensez à utiliser `pygame.display.flip()` pour mettre à jour l'affichage.
- Pour les animations, vous pouvez jouer avec les couleurs ou la position des éléments entre les frames.

### Intégration avec le code existant

- Créez une nouvelle classe (par exemple `InterfaceGraphique`) pour gérer l'affichage.
- Modifiez la classe `ClientDefiMot` pour utiliser cette nouvelle interface graphique.
- Assurez-vous que l'affichage est mis à jour à chaque changement d'état reçu du serveur.

### Résultat attendu

À la fin de cette extension, votre jeu devrait avoir une interface graphique fonctionnelle montrant en temps réel le mot mystère, les scores des joueurs et le temps restant. Les joueurs devraient pouvoir interagir avec le jeu via cette interface, rendant l'expérience plus immersive et visuelle.

Cette extension optionnelle permet non seulement d'améliorer l'aspect visuel du jeu, mais aussi d'explorer les concepts de base du développement d'interfaces graphiques en Python, ajoutant ainsi une compétence précieuse à votre répertoire de programmation.
