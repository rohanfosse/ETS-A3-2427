import requests
import random
import argparse

def generer_liste_mots(taille_min, taille_max, nombre_mots):
    """
    Génère une liste de mots en fonction de la taille minimale, maximale et du nombre demandé.
    Les mots sont récupérés depuis une source en ligne.

    :param taille_min: Taille minimale des mots.
    :param taille_max: Taille maximale des mots.
    :param nombre_mots: Nombre de mots à générer.
    :return: Liste des mots générés.
    """
    url = "https://raw.githubusercontent.com/words/fr-classification-data/master/data/fr.txt"
    
    try:
        # Récupération de la liste de mots en ligne
        response = requests.get(url)
        response.raise_for_status()
        tous_les_mots = response.text.split('\n')
        
        # Filtrage des mots selon les critères de taille et exclusion des caractères spéciaux
        mots_filtres = [mot.upper() for mot in tous_les_mots if taille_min <= len(mot) <= taille_max and mot.isalpha()]
        
        # Sélection aléatoire du nombre de mots demandé
        mots_selectionnes = random.sample(mots_filtres, min(nombre_mots, len(mots_filtres)))
        
        return mots_selectionnes
    
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des mots : {e}")
        return []

def sauvegarder_mots(mots, nom_fichier):
    """
    Sauvegarde une liste de mots dans un fichier texte.

    :param mots: Liste des mots à sauvegarder.
    :param nom_fichier: Nom du fichier dans lequel sauvegarder les mots.
    """
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        for mot in mots:
            f.write(mot + '\n')

def main():
    """
    Point d'entrée principal du script. Gère les arguments en ligne de commande et exécute les fonctions nécessaires.
    """
    # Configuration des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Génère une liste de mots pour le Défi du Mot Mystère")
    parser.add_argument("-n", "--nombre", type=int, default=100, help="Nombre de mots à générer (défaut : 100)")
    parser.add_argument("-min", "--taille_min", type=int, default=4, help="Taille minimale des mots (défaut : 4)")
    parser.add_argument("-max", "--taille_max", type=int, default=12, help="Taille maximale des mots (défaut : 12)")
    parser.add_argument("-o", "--output", default="mots.txt", help="Nom du fichier de sortie (défaut : mots.txt)")

    args = parser.parse_args()

    # Génération et sauvegarde des mots
    liste_mots = generer_liste_mots(args.taille_min, args.taille_max, args.nombre)
    
    if liste_mots:
        sauvegarder_mots(liste_mots, args.output)
        print(f"{len(liste_mots)} mots ont été générés et sauvegardés dans {args.output}")
    else:
        print("Aucun mot n'a été généré. Vérifiez vos paramètres ou votre connexion Internet.")

if __name__ == "__main__":
    main()
