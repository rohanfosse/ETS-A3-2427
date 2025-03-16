# **📜 Projet d'IA – "Création d'un Joueur Virtuel pour le Défi du Mot Mystère"** 🤖🧠

📁 **Fichier principal : `joueur_virtuel.py`**  
📄 **Fichier : `Phase_4_Consignes.pdf`**

---

## **🌍 Contexte**

Dans ce projet, vous allez concevoir un **joueur virtuel** capable de jouer au "Défi du Mot Mystère". Ce joueur devra utiliser des stratégies algorithmiques pour deviner les mots mystères de manière efficace. À la fin, vos joueurs virtuels s’affronteront dans un tournoi pour déterminer la meilleure stratégie. En option, vous pourrez également permettre à vos IA de coopérer ou de s’affronter en ligne grâce à un mode multijoueur basé sur les sockets.

---

## **1️⃣ Objectifs pédagogiques**

- Décomposer un problème complexe en sous-problèmes gérables.
- Concevoir des algorithmes pour résoudre des problèmes spécifiques.
- Étudier et analyser la complexité algorithmique des solutions proposées.
- Comparer différentes stratégies dans un environnement compétitif.
- (Optionnel) Implémenter une communication réseau entre IA pour un mode multijoueur.

---

## **2️⃣ Fonctionnalités attendues**

Vous devez implémenter une classe `JoueurVirtuel` qui représente un joueur intelligent capable de jouer au "Défi du Mot Mystère". Cette classe doit inclure les fonctionnalités suivantes :

1. **Analyse des fréquences des lettres** : Identifier les lettres les plus fréquentes dans le dictionnaire pour guider les propositions.
2. **Filtrage des mots possibles** : Réduire la liste des mots candidats en fonction du mot partiellement dévoilé.
3. **Proposition de lettres et de mots** : Décider si le joueur propose une lettre ou tente de deviner un mot entier.
4. **Gestion de la mémoire** : Retenir les mots déjà rencontrés pour améliorer l'efficacité au fil des parties.
5. **Stratégie adaptative** : Ajuster les décisions en fonction des résultats obtenus.

En option, vos IA pourront coopérer ou s’affronter en ligne dans un mode multijoueur.

---

## **3️⃣ Structure du code attendu**

Voici une architecture de base pour structurer votre code :

```python
class JoueurVirtuel:
    def __init__(self, dictionnaire):
        """
        Initialise le joueur virtuel avec un dictionnaire de mots.
        :param dictionnaire: Liste de mots disponibles dans le jeu.
        """
        pass

    def analyser_frequences_lettres(self):
        """
        Analyse la fréquence des lettres dans le dictionnaire et stocke les résultats.
        """
        pass

    def filtrer_mots_possibles(self, mot_actuel):
        """
        Filtre les mots du dictionnaire correspondant au motif actuel.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :return: Liste des mots possibles.
        """
        pass

    def choisir_meilleure_lettre(self, mot_actuel, lettres_essayees):
        """
        Choisit la meilleure lettre à proposer en fonction des lettres déjà essayées.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :param lettres_essayees: Lettres déjà proposées.
        :return: Une lettre à essayer.
        """
        pass

    def evaluer_risque_mot_entier(self, mot_actuel):
        """
        Évalue le risque de proposer un mot entier en fonction des mots possibles restants.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :return: Un booléen indiquant si proposer un mot entier est raisonnable.
        """
        pass

    def proposer_lettre(self, mot_actuel, lettres_essayees):
        """
        Propose une lettre à essayer.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :param lettres_essayees: Lettres déjà proposées.
        :return: Une lettre à essayer.
        """
        pass

    def proposer_mot(self, mot_actuel):
        """
        Propose un mot entier si le risque est acceptable.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :return: Un mot entier ou None si aucune proposition n'est faite.
        """
        pass

    def mise_a_jour(self, resultat):
        """
        Met à jour la mémoire et les stratégies en fonction du résultat précédent.
        :param resultat: Dictionnaire contenant des informations sur la validité de l'action précédente.
                         Exemple: {"action": "lettre", "valide": True, "mot": "_ A _ _ E"}
        """
        pass

    def jouer_tour(self, mot_actuel, lettres_essayees, temps_restant):
        """
        Décide de l'action à effectuer pour ce tour (proposer une lettre ou un mot).
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :param lettres_essayees: Lettres déjà proposées.
        :param temps_restant: Temps restant pour deviner le mot (en secondes).
        :return: Une action sous forme de tuple ("lettre", "A") ou ("mot", "APPLE").
        """
        pass
```

---

## **4️⃣ Étapes et indices**

### **Étape 1 – Analyse des fréquences des lettres**

- Objectif : Identifier les lettres les plus fréquentes dans le dictionnaire pour guider les propositions du joueur virtuel.
- Indices :
  - Pensez à parcourir tous les mots du dictionnaire et à compter combien de fois chaque lettre apparaît. Une structure comme un dictionnaire Python peut être utile ici.

---

### **Étape 2 – Filtrage des mots possibles**

- Objectif : Réduire la liste des mots candidats en fonction du motif actuel (exemple : `_ A _ _ E`).
- Indices :
  - Imaginez que chaque `_` représente une lettre inconnue. Comment pourriez-vous vérifier si un mot correspond au motif ?
  - Les expressions régulières peuvent être utiles ici.

---

### **Étape 3 – Proposition d’une lettre**

- Objectif : Choisir la prochaine lettre à proposer parmi celles qui n’ont pas encore été essayées.
- Indices :
  - En utilisant les fréquences calculées à l’étape 1, quelle lettre non encore essayée maximiserait vos chances ?
  - Pensez également à éviter les doublons.

---

### **Étape 4 – Proposition d’un mot entier**

- Objectif : Décider s’il est raisonnable de tenter un mot entier et lequel proposer.
- Indices :
  - Si vous n’avez qu’un ou deux mots possibles après filtrage, cela pourrait être une bonne idée d’essayer directement un mot entier.

---

### **Étape 5 – Mémoire et adaptation**

- Objectif : Améliorer l’efficacité au fil des parties en mémorisant les succès et échecs précédents.
- Indices :
  - Vous pouvez utiliser une structure comme un dictionnaire Python pour associer chaque mot mystère rencontré à sa solution correcte.

---

## **5️⃣ Section optionnelle – Mode multijoueur avec sockets**

Pour aller plus loin, vous pouvez permettre à vos IA :

1. De coopérer pour deviner ensemble un maximum de mots dans un temps imparti (mode coopératif).
2. De s’affronter directement pour voir laquelle devine le plus rapidement (mode compétitif).

### Mise en œuvre :

1. Reprenez le code serveur/client basé sur les sockets proposé dans le sujet précédent :

   - Le serveur gère l’état global du jeu (mot mystère, scores).
   - Les clients représentent vos IA qui communiquent avec le serveur via sockets.

2. Adaptez votre classe `JoueurVirtuel` pour qu’elle puisse interagir avec le serveur :

   - Envoyer ses propositions (lettres ou mots) au serveur.
   - Recevoir l’état mis à jour du jeu depuis le serveur.

3. Organisez une simulation où plusieurs IA coopèrent ou s’affrontent en ligne.

---

## **6️⃣ Tournoi final**

### Règles :

1. Chaque joueur virtuel joue contre tous les autres joueurs sur un ensemble fixe de mots mystères.
2. Les parties peuvent être locales ou en ligne via sockets (si vous avez implémenté l’option).
3. Le joueur qui devine le plus de mots gagne la partie.

### Critères d’évaluation :

- Nombre total de mots devinés.
- Temps moyen par mot deviné.
- Taux d’erreur (propositions incorrectes).

---
