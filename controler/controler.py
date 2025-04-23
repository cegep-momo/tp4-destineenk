import threading
from model.platine import Platine
from model.mesure import Modele

class Controleur:
    def __init__(self):
        self.thread = None #stock le thread
        self.platine = Platine()
        self.model = Modele("./donnees.json")
    

        
    def demarrer_thread(self):
        if self.thread is None:
            self.thread = threading.Thread(target=self.platine.appuyer_bouton, daemon = True)
            self.thread.start()
        else:
            self.enregister_lesdonnees()
            
    def enregister_lesdonnees(self):
        mesures = self.platine.get_liste_mesure()
        if mesures:
            try:
                for distances in mesures:
                    self.model.creer_mesure(distances)
                print(f"Mesures à enregistrer: {self.model.mesures}")  # Vérifie ce que tu enregistres

                self.model.enregister_donnees()
                self.platine.vider_mesures()
            except Exception as e:
                print("Erreur lors de lenregistrement des donnees: {e}")
    
            
    