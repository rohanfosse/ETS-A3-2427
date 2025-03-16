class CompteBancaire:
    def __init__(self, solde):
        self.__solde = solde  # Attribut privé

    def deposer(self, montant):
        self.__solde += montant

    def retirer(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants.")

    def afficher_solde(self):
        return f"Solde : {self.__solde}€"

compte = CompteBancaire(100)
compte.deposer(50)
compte.retirer(30)
print(compte.afficher_solde())
