class Observateur:
    def mise_a_jour(self, message):
        pass

class Sujet:
    def __init__(self):
        self.observateurs = []

    def ajouter_observateur(self, obs):
        self.observateurs.append(obs)

    def notifier(self, message):
        for obs in self.observateurs:
            obs.mise_a_jour(message)

class ObservateurConcret(Observateur):
    def mise_a_jour(self, message):
        print(f"Notification reçue : {message}")

sujet = Sujet()
obs1 = ObservateurConcret()
sujet.ajouter_observateur(obs1)

sujet.notifier("Nouvelle mise à jour disponible")
