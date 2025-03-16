import unittest
from joueur_virtuel import JoueurVirtuel

class TestJoueurVirtuel(unittest.TestCase):
    def setUp(self):
        dictionnaire = ["PYTHON", "MYSTERE", "PROGRAMME", "VIRTUEL"]
        self.joueur = JoueurVirtuel(dictionnaire)

    def test_analyser_frequences_lettres(self):
        frequences_attendues = {"P": 1, "Y": 1, "T": 2, "H": 1, "O": 1,
                                "M": 3, "S": 1, "E": 4, "R": 3, "G": 1,
                                "A": 1, "V": 1, "I": 1, "U": 1, "L": 1}
        
        self.assertEqual(self.joueur.frequences_lettres, frequences_attendues)

    def test_filtrer_mots_possibles(self):
        mots_possibles = self.joueur.filtrer_mots_possibles("_ Y T _ _ _")
        self.assertEqual(mots_possibles, ["PYTHON"])

    def test_choisir_meilleure_lettre(self):
        lettre = self.joueur.choisir_meilleure_lettre("_ Y T _ _ _", ["P"])
        self.assertEqual(lettre, "H")

    def test_evaluer_risque_mot_entier(self):
        risque = self.joueur.evaluer_risque_mot_entier("_ Y T _ _ _")
        self.assertTrue(risque)

    def test_proposer_mot(self):
        mot = self.joueur.proposer_mot("_ Y T _ _ _")
        self.assertEqual(mot, "PYTHON")


if __name__ == "__main__":
    unittest.main()
