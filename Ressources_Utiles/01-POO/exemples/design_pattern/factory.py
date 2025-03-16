class Vehicule:
    def decrire(self):
        pass

class Voiture(Vehicule):
    def decrire(self):
        return "Ceci est une voiture."

class Moto(Vehicule):
    def decrire(self):
        return "Ceci est une moto."

class VehiculeFactory:
    @staticmethod
    def creer_vehicule(type_vehicule):
        if type_vehicule == "voiture":
            return Voiture()
        elif type_vehicule == "moto":
            return Moto()
        else:
            raise ValueError("Type inconnu")

v = VehiculeFactory.creer_vehicule("voiture")
print(v.decrire())
