# 🤖 **Projet d'IA – Création d'un Joueur Virtuel pour Battle Ship Royale** 🧠

📁 **Fichier principal : `joueur_virtuel.py`**  
📄 **Fichier : `Phase_3_Consignes.pdf`**

---

## 🌍 **Contexte**

Dans ce projet, vous allez concevoir un **joueur virtuel** capable de jouer au "Battle Ship Royale". Ce joueur devra utiliser des stratégies algorithmiques pour placer ses bateaux, analyser la grille adverse et tirer de manière efficace. À la fin, vos joueurs virtuels s’affronteront dans un tournoi pour déterminer la meilleure stratégie. En option, vous pourrez également permettre à vos IA de s’affronter en réseau grâce à un mode multijoueur basé sur les sockets.

---

## **Objectifs pédagogiques**

- Décomposer un problème complexe en sous-problèmes gérables.
- Concevoir des algorithmes pour résoudre des problèmes spécifiques.
- Étudier et analyser la complexité algorithmique des solutions proposées.
- Comparer différentes stratégies dans un environnement compétitif.
- (Optionnel) Implémenter une communication réseau entre IA pour un mode multijoueur.

---

## **Fonctionnalités attendues**

Vous devez implémenter une classe `JoueurVirtuel` représentant un joueur intelligent capable de jouer à "Battle Ship Royale". Cette classe doit inclure les fonctionnalités suivantes :

1. **Placement stratégique des bateaux** : Choisir les meilleures positions pour minimiser les risques.
2. **Analyse des tirs précédents** : Identifier les zones les plus prometteuses à cibler.
3. **Choix intelligent des tirs** : Décider où tirer pour maximiser les chances de toucher un bateau adverse.
4. **Gestion de la mémoire** : Retenir les résultats des tirs précédents pour améliorer la stratégie.
5. **Stratégie adaptative** : Ajuster les décisions en fonction des résultats obtenus.

En option, vos IA pourront s’affronter en réseau dans un mode multijoueur.

---

## **Structure du code attendu**

Voici une architecture de base pour structurer votre code :

```python
class JoueurVirtuel:
    def __init__(self, taille_grille):
        """
        Initialise le joueur virtuel avec une grille.
        :param taille_grille: Taille de la grille (ex: 5 pour une grille 5x5).
        """
        pass

    def placer_bateaux(self):
        """
        Place stratégiquement les bateaux sur la grille.
        """
        pass

    def analyser_tirs_precedents(self, historique_tirs):
        """
        Analyse l'historique des tirs pour améliorer la stratégie.
        :param historique_tirs: Liste des tirs déjà effectués avec résultats.
        """
        pass

    def choisir_position_tir(self, historique_tirs):
        """
        Choisit la meilleure position pour le prochain tir.
        :param historique_tirs: Liste des tirs déjà effectués avec résultats.
        :return: Coordonnées du prochain tir (ligne, colonne).
        """
        pass

    def mise_a_jour_strategie(self, resultat_tir):
        """
        Met à jour la stratégie selon le résultat du tir précédent.
        :param resultat_tir: Résultat du tir précédent.
        """
        pass

    def jouer_tour(self, historique_tirs):
        """
        Décide de l'action pour ce tour (position de tir).
        :param historique_tirs: Historique complet des tirs.
        :return: Coordonnées du tir choisi (ligne, colonne).
        """
        pass
```

---

## **Étapes et indices**

### **Étape 1 – Placement stratégique des bateaux**

- Objectif : Positionner les bateaux pour minimiser les risques.
- Indices : Répartissez vos bateaux pour éviter les regroupements faciles à détecter.

---

### **Étape 2 – Analyse des tirs précédents**

- Objectif : Identifier les zones à cibler en priorité.
- Indices : Utilisez les résultats antérieurs (touchés/manqués) pour adapter vos tirs suivants.

---

### **Étape 3 – Choix intelligent des tirs**

- Objectif : Maximiser les chances de toucher un bateau.
- Indices : Après un tir touché, essayez les cases voisines en priorité.

---

### **Étape 4 – Mémoire et adaptation**

- Objectif : Améliorer l'efficacité en mémorisant les succès et échecs.
- Indices : Stockez l'historique des résultats pour éviter les répétitions inutiles.

---

## **Section optionnelle – Mode multijoueur avec sockets**

Vous pouvez permettre à vos IA de s’affronter directement en réseau :

### Mise en œuvre :

1. Utilisez le code serveur/client avec sockets de la phase précédente.
   - Le serveur coordonne les parties.
   - Les clients représentent vos IA communiquant via sockets.

2. Adaptez votre classe `JoueurVirtuel` pour interagir avec le serveur :
   - Envoyer les tirs au serveur.
   - Recevoir l'état du jeu du serveur.

3. Organisez un tournoi en réseau entre plusieurs IA.

---

## **Tournoi final**

### Règles :

1. Chaque joueur virtuel affronte les autres dans des parties définies.
2. Les parties peuvent être locales ou réseau (optionnel).
3. Le joueur qui coule le plus vite les bateaux adverses remporte la victoire.

### Critères d’évaluation :

- Nombre de victoires.
- Nombre moyen de tirs nécessaires pour gagner.
- Précision (rapport tirs touchés/tirs totaux).

---

**Bonne programmation !**