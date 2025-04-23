from gpiozero import Button, DistanceSensor
import LCD1602 
from time import sleep
from view.view import Vue

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
        self.vue = Vue()
        self.liste_mesure = []
    
    def appuyer_bouton(self):
        while True:
            if self.bouton_demarrer.is_pressed:
                self.systeme_demarrer = not self.systeme_demarrer
                if self.systeme_demarrer:
                    self.vue.message_activation()                         
                else:
                    self.vue.message_arret()
                    self.mesure = False
                    self.vue.desactivation_mesure()
                sleep(1)
                
            if self.systeme_demarrer and self.bouton_mesure.is_pressed:
                self.vue.message_mesure()
                self.mesure = True
                sleep(1)
                while self.bouton_mesure.is_pressed:
                    sleep(0.1)
                
            if self.systeme_demarrer and self.mesure:
                self.cm = round(self.capteur.distance * 100)
                self.vue.message_distance(self.cm)
                self.liste_mesure.append(self.cm)
                sleep(5)
            sleep(0.1)
            
    def get_liste_mesure(self):
        return self.liste_mesure
   
                
                            
        