# Battle Ship Royale Solo - Squelette initial du code

import random

# Constantes globales
TAILLE_GRILLE = 5
NOMBRE_BATEAUX = 3

def creer_grille():
    """Créer une grille vide initiale."""
    pass

def afficher_grille(grille, afficher_bateaux=False):
    """Afficher la grille à l'écran."""
    pass

def placer_bateaux_joueur(grille):
    """Permettre au joueur de placer ses bateaux sur la grille."""
    pass

def placer_bateaux_aleatoires(grille):
    """Placer aléatoirement les bateaux adverses."""
    pass

def effectuer_tir(grille, ligne, colonne):
    """Effectuer un tir sur une position et retourner le résultat (touché, coulé, manqué)."""
    pass

def verifier_fin_partie(grille):
    """Vérifier si tous les bateaux sont coulés."""
    pass

def tour_joueur(grille_adverse):
    """Gérer le tour du joueur : saisie du tir, vérification et résultat."""
    pass

def tour_adversaire(grille_joueur):
    """Gérer le tir de l'adversaire virtuel (aléatoire)."""
    pass

def afficher_resultat_final(nombre_tirs):
    """Afficher le résultat final et le score de la partie."""
    pass

def main():
    """Fonction principale qui lance le jeu."""
    grille_joueur = creer_grille()
    grille_adverse = creer_grille()

    placer_bateaux_joueur(grille_joueur)
    placer_bateaux_aleatoires(grille_adverse)

    nombre_tirs = 0
    partie_terminee = False

    while not partie_terminee:
        afficher_grille(grille_adverse)
        tour_joueur(grille_adverse)
        nombre_tirs += 1

        if verifier_fin_partie(grille_adverse):
            partie_terminee = True
            print("Félicitations, vous avez gagné !")
            break

        tour_adversaire(grille_joueur)
        if verifier_fin_partie(grille_joueur):
            partie_terminee = True
            print("Dommage, l'adversaire a gagné !")

    afficher_resultat_final(nombre_tirs)

if __name__ == "__main__":
    main()
