from gpiozero import Button, DistanceSensor
from view import LCD1602 
from time import sleep

class Platine:
    def __init__(self):
    #initialisation des boutons
        self.bouton_demarrer = Button(23) # permet de demarrer et arreter le systeme
        self.bouton_mesure = Button(24) # permet de orendre la mesure
        self.systeme_demarrer = False # systeme en marche
        self.mesure = False
        self.lcd = LCD1602
        self.lcd.init(0x27,1) #initialisation de ecran
        self.capteur = DistanceSensor(echo = 12, trigger = 17)
    
    def appuyer_bouton(self):
        while True:
            if self.bouton_demarrer.is_pressed:
                self.systeme_demarrer = not self.systeme_demarrer
                if self.systeme_demarrer:
                    self.lcd.write(0,0, "Systeme actif")
                    self.lcd.write(1,1, " ")                              
                else:
                    self.lcd.write(0,0, "Systeme arrete")
                    self.lcd.write(1,1, " ")
                    self.mesure = False
                sleep(1)
                
            if self.systeme_demarrer and self.bouton_mesure.is_pressed:
                self.lcd.write(0,0, "Mesure active")
                self.lcd.write(1,1, "    ")
                sleep(1)
                self.mesure = True
                  
                while self.bouton_mesure.is_pressed:
                    sleep(0.5)
                sleep(0.5)
                
            if self.systeme_demarrer and self.mesure:
                self.cm = round(self.capteur.distance * 100)
                self.lcd.write(0,0, "Distance")
                self.lcd.write(1,1, f"{self.cm} cm")
                sleep(5)
            sleep(0.1)
                    
                
                            
        