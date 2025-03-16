import tkinter as tk
from tkinter import ttk
import json
import socket
import threading

class InterfaceGraphiqueTournoi:
    def __init__(self, master):
        self.master = master
        self.master.title("Tournoi du Défi du Mot Mystère")
        self.master.geometry("800x600")

        self.setup_ui()
        self.scores = {}
        self.mot_actuel = ""
        self.temps_restant = 120

        # Configuration du socket client
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connecter_au_serveur()

        # Démarrer la réception des mises à jour dans un thread séparé
        threading.Thread(target=self.recevoir_mises_a_jour, daemon=True).start()

    def setup_ui(self):
        # Frame principale
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Temps restant
        self.temps_label = ttk.Label(main_frame, text="Temps restant : 120s", font=("Arial", 16))
        self.temps_label.pack(pady=10)

        # Mot actuel
        self.mot_label = ttk.Label(main_frame, text="Mot actuel : ________", font=("Arial", 20))
        self.mot_label.pack(pady=20)

        # Tableau des scores
        self.tree = ttk.Treeview(main_frame, columns=('Joueur', 'Score'), show='headings')
        self.tree.heading('Joueur', text='Joueur')
        self.tree.heading('Score', text='Score')
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Scrollbar pour le tableau
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def connecter_au_serveur(self):
        try:
            self.socket.connect(('localhost', 12345))  # Remplacez par l'adresse et le port de votre serveur
            print("Connecté au serveur")
        except Exception as e:
            print(f"Erreur de connexion au serveur : {e}")

    def recevoir_mises_a_jour(self):
        while True:
            try:
                data = self.socket.recv(1024).decode()
                if not data:
                    break
                self.traiter_mise_a_jour(json.loads(data))
            except Exception as e:
                print(f"Erreur de réception : {e}")
                break

    def traiter_mise_a_jour(self, data):
        self.master.after(0, self.mettre_a_jour_interface, data)

    def mettre_a_jour_interface(self, data):
        # Mise à jour du temps
        self.temps_restant = data.get('temps_restant', self.temps_restant)
        self.temps_label.config(text=f"Temps restant : {self.temps_restant}s")

        # Mise à jour du mot actuel
        self.mot_actuel = data.get('mot_actuel', self.mot_actuel)
        self.mot_label.config(text=f"Mot actuel : {self.mot_actuel}")

        # Mise à jour des scores
        nouveaux_scores = data.get('scores', {})
        if nouveaux_scores != self.scores:
            self.scores = nouveaux_scores
            self.mettre_a_jour_tableau_scores()

    def mettre_a_jour_tableau_scores(self):
        # Effacer le tableau actuel
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Ajouter les nouveaux scores
        for joueur, score in sorted(self.scores.items(), key=lambda x: x[1], reverse=True):
            self.tree.insert('', tk.END, values=(joueur, score))

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGraphiqueTournoi(root)
    root.mainloop()
