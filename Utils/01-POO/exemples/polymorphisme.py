class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom}, {self.age} ans"

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age

p1 = Personne("Alice", 30)
p2 = Personne("Alice", 30)
print(p1)  # Utilise __str__()
print(p1 == p2)  # Utilise __eq__()
