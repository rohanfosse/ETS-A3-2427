class Moteur:
    def demarrer(self):
        return "Moteur en marche"

class Voiture:
    def __init__(self):
        self.moteur = Moteur()  # Composition

    def demarrer(self):
        return self.moteur.demarrer()

v = Voiture()
print(v.demarrer())  # "Moteur en marche"
