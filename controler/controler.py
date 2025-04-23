from model.platine import Platine
from model.mesure import Mesure
import threading

class Controleur:
    def __init__(self):
        self.platine = Platine()
        self.thread = None


         
    def demarrer_thread(self):
        if self.thread is None:
            self.thread = threading.Thread(target=self.platine.lire_valeurs, daemon = True)
            self.thread.start()
            self.platine.lire_valeurs
        else :
            self.arreter_systeme()
            
    def arreter_systeme(self):
        self.thread.join()
            
        
  
                
    
   
    