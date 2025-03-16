class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être implémentée")

class Chien(Animal):
    def parler(self):
        return "Wouf !"

class Chat(Animal):
    def parler(self):
        return "Miaou !"

animaux = [Chien(), Chat()]
for animal in animaux:
    print(animal.parler())

# Héritage multiple
class A:
    def afficher(self):
        return "Classe A"

class B:
    def afficher(self):
        return "Classe B"

class C(A, B):  # Hérite de A et B
    pass

c = C()
print(c.afficher())  # Affiche "Classe A" (ordre de résolution des méthodes)
