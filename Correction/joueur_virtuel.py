class JoueurVirtuel:
    def __init__(self, dictionnaire):
        """
        Initialise le joueur virtuel avec un dictionnaire de mots.
        :param dictionnaire: Liste de mots disponibles dans le jeu.
        """
        self.dictionnaire = dictionnaire
        self.frequences_lettres = {}
        self.memoire = {}
        self.analyser_frequences_lettres()

    def analyser_frequences_lettres(self):
        """
        Analyse la fréquence des lettres dans le dictionnaire et stocke les résultats.
        """
        from collections import Counter
        toutes_les_lettres = "".join(self.dictionnaire)
        self.frequences_lettres = dict(Counter(toutes_les_lettres))

    def filtrer_mots_possibles(self, mot_actuel):
        """
        Filtre les mots du dictionnaire correspondant au motif actuel.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :return: Liste des mots possibles.
        """
        import re
        motif = mot_actuel.replace("_", ".")
        return [mot for mot in self.dictionnaire if re.fullmatch(motif, mot)]

    def choisir_meilleure_lettre(self, mot_actuel, lettres_essayees):
        """
        Choisit la meilleure lettre à proposer en fonction des lettres déjà essayées.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :param lettres_essayees: Lettres déjà proposées.
        :return: Une lettre à essayer.
        """
        mots_possibles = self.filtrer_mots_possibles(mot_actuel)
        compteur = {}
        
        for mot in mots_possibles:
            for lettre in mot:
                if lettre not in lettres_essayees:
                    compteur[lettre] = compteur.get(lettre, 0) + 1

        # Retourne la lettre la plus fréquente parmi les mots possibles
        return max(compteur, key=compteur.get, default=None)

    def evaluer_risque_mot_entier(self, mot_actuel):
        """
        Évalue le risque de proposer un mot entier en fonction des mots possibles restants.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :return: Un booléen indiquant si proposer un mot entier est raisonnable.
        """
        mots_possibles = self.filtrer_mots_possibles(mot_actuel)
        return len(mots_possibles) <= 2

    def proposer_lettre(self, mot_actuel, lettres_essayees):
        """
        Propose une lettre à essayer.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :param lettres_essayees: Lettres déjà proposées.
        :return: Une lettre à essayer.
        """
        return self.choisir_meilleure_lettre(mot_actuel, lettres_essayees)

    def proposer_mot(self, mot_actuel):
        """
        Propose un mot entier si le risque est acceptable.
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :return: Un mot entier ou None si aucune proposition n'est faite.
        """
        mots_possibles = self.filtrer_mots_possibles(mot_actuel)
        
        if len(mots_possibles) == 1:
            return mots_possibles[0]
        
    def mise_a_jour(self, resultat):
        """
        Met à jour la mémoire et les stratégies en fonction du résultat précédent.
        :param resultat: Dictionnaire contenant des informations sur la validité de l'action précédente.
                         Exemple: {"action": "lettre", "valide": True, "mot": "_ A _ _ E"}
                         Exemple: {"action": "mot", "valide": False}
                         Exemple: {"action": "mot", "valide": True, "mot_final": "MYSTERE"}
        """
        if resultat["action"] == "mot" and resultat.get("valide"):
            mot_final = resultat.get("mot_final")
            if mot_final:
                self.memoire[mot_final] = True

    def jouer_tour(self, mot_actuel, lettres_essayees, temps_restant):
        """
        Décide de l'action à effectuer pour ce tour (proposer une lettre ou un mot).
        :param mot_actuel: Mot partiellement dévoilé (ex: "_ A _ _ E").
        :param lettres_essayees: Lettres déjà proposées.
        :param temps_restant: Temps restant pour deviner le mot (en secondes).
        :return: Une action sous forme de tuple ("lettre", "A") ou ("mot", "APPLE").
        """
        if self.evaluer_risque_mot_entier(mot_actuel):
            mot = self.proposer_mot(mot_actuel)
            if mot:
                return ("mot", mot)
        
        lettre = self.proposer_lettre(mot_actuel, lettres_essayees)
        if lettre:
            return ("lettre", lettre)

        return None  # Si aucune action ne peut être prise
