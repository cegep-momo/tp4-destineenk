import threading
from model.platine import Platine
from model.mesure import Mesure

class Controleur:
    def __init__(self):
        self.thread = None #stock le thread
        self.platine = Platine()
    

        
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
                for distance in mesures:
                    mesure = Mesure(distance)
                    mesure.sauvegarderJson()
            except Exception as e:
                print("Erreur lors de lenregistrement des donnees: {e}")
    
            
    