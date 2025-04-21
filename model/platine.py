from gpiozero import Button, DistanceSensor
from view import LCD1602 
from time import sleep

class Platine:
    def __init__(self):
    #initialisation des boutons
        self.bouton_demarrer = Button(23) # permet de demarrer et arreter le systeme
        self.bouton_mesure = Button(24) # permet de orendre la mesure
        self.systeme_demarrer = False # systeme en marche
        LCD1602.init(0x27,1) #initialisation de ecran
        self.capteur = DistanceSensor(echo = 12, trigger = 17, max_distance = 3)
    
    def appuyer_bouton(self):
        while True:
            if self.bouton_demarrer.is_pressed:
                if not self.systeme_demarrer:
                    self.systeme_demarrer = True
                    print("Le systeme est demarre")
                    self.cm = self.capteur.distance * 100
                    LCD1602.write(0x0, "Distance")
                    LCD1602.write(0x1, f"{self.cm} cm")
                    
                    sleep(1)
                    
                else:
                    print("Le systeme est deja en cours")
                sleep(0.5)
            sleep(0.5)
            
        