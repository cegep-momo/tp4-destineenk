import threading
from model.platine import Platine

class Controleur:
    def __init__(self):
        self.thread = None #stock le thread
        self.platine = Platine()
        
    def demarrer_thread(self):
        if self.thread is None:
            self.thread = threading.Thread(target=self.platine.appuyer_bouton, daemon = True)
            self.thread.start()
    
            
    