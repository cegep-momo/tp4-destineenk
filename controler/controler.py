import threading
from model.platine import Platine
from model.mesure import Modele

class Controleur:
    def __init__(self):
        self.thread = None #stock le thread
        self.platine = Platine()
        self.model = Modele("donnees.json")

        
    def demarrer_thread(self):
        if self.thread is None:
            self.thread = threading.Thread(target=self.platine.appuyer_bouton, daemon = True)
            self.thread.start()
        else:
                self.enregister_donnees()
            
    def enregister_donnees(self):
        mesures = self.platine.get_liste_mesure()
        if mesures:
            try:
                for distances in mesures:
                    self.model.creer_mesure(distances)
                self.model.enregister_donnees()
                self.platine.vider_mesures()
            except Exception as e:
                print("Erreur lors de lenregistrement des donnees: {e}")
    
            
    