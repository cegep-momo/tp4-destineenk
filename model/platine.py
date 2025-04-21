from gpiozero import Button
from time import sleep

class Platine:
    def __init__(self):
    #initialisation des boutons
        self.bouton_demarrer = Button(23) # permet de demarrer et arreter le systeme
        self.bouton_mesure = Button(24) # permet de orendre la mesure
        self.systeme_demarrer = False # systeme en marche
    
    def appuyer_bouton(self):
        while True:
            if self.bouton_demarrer.is_pressed:
                if not self.systeme_demarrer:
                    self.systeme_demarrer = True
                    print("Le systeme est demarre")
                else:
                    print("Le systeme est deja en cours")
                sleep(0.5)
            sleep(0.5)
            
        