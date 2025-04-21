import threading
from view import LCD1602 
from model.platine import Platine

class Controleur:
    def __init__(self):
        self.thread = None #stock le thread
        self.platine = Platine()
        LCD1602.init(0x27,1) #initialisation de ecran
        
    def demarrer_thread(self):
        print("test")
        if self.thread is None:
            print("test")
            self.thread = threading.Thread(target=self.platine.appuyer_bouton, daemon = True)
            self.thread.start()
        else:
            print("thread deja en cours")
            
    