import random
import time

def charger_mots(fichier):
    """Charge les mots depuis un fichier texte."""
    with open(fichier, 'r') as f:
        mots = f.read().splitlines()
    return mots

def choisir_mot(mots):
    """Choisit un mot aléatoirement dans la liste des mots."""
    return random.choice(mots)

def afficher_mot(mot, lettres_trouvees):
    """Affiche le mot avec les lettres trouvées et des underscores pour les lettres manquantes."""
    return ' '.join([lettre if lettre in lettres_trouvees else '_' for lettre in mot])

# D'autres fonctions à ajouter ici

def jouer():
    """Fonction principale pour jouer au jeu."""
    mots = charger_mots('mots.txt')
    mot_a_deviner = choisir_mot(mots)


if __name__ == "__main__":
    jouer()