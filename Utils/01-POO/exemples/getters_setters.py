class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.__salaire = salaire

    @property
    def salaire(self):
        """Getter : retourne le salaire"""
        return self.__salaire

    @salaire.setter
    def salaire(self, montant):
        """Setter : modifie le salaire uniquement si positif"""
        if montant >= 0:
            self.__salaire = montant
        else:
            raise ValueError("Le salaire ne peut pas être négatif.")

e = Employe("Alice", 3000)
print(e.salaire)  # Accès via le getter
e.salaire = 3500  # Modification via le setter
