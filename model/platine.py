from gpiozero import Button, DistanceSensor
from time import sleep
from view.view import Vue
from time import sleep
from view.view import Vue
from model.mesure import Mesure

class Platine:
    def __init__(self):
       
        self.systeme_demarrer = False # systeme en marche
        self.mesure = False
        self.capteur = DistanceSensor(echo = 16, trigger = 17)
        self.vue = Vue()
        self.liste_mesure = []
        self.bouton_demarrer = Button(23) 
        self.bouton_mesure = Button(24) 
        
    def lire_valeurs(self):
          while True:
            if self.bouton_demarrer.is_pressed:
                self.systeme_demarrer = not self.systeme_demarrer
                if self.systeme_demarrer:
                    self.vue.message_activation()                         
                else:
                    self.arreter_lecture()
                sleep(1)
                
            if self.systeme_demarrer and self.bouton_mesure.is_pressed:
                self.vue.message_mesure()
                self.mesure = True
                sleep(1)
                while self.bouton_mesure.is_pressed:
                    sleep(0.1)
                
            if self.systeme_demarrer and self.mesure:
                self.cm = round(self.capteur.distance * 100, 2)
                self.vue.message_distance(self.cm)
                self.liste_mesure.append(self.cm)
                sleep(5)
                
    def arreter_lecture(self):
        self.vue.message_arret()
        sleep(1)
        self.mesure = False
        self.vue.desactivation_mesure()
        print("Sauvegarde des mesures")
        for distance in self.liste_mesure:
            mesure = Mesure(distance)
            mesure.sauvegarderJson()
        print("Sauvegarde terminee")
        
   
    def get_liste_mesure(self):
        return self.liste_mesure
    
        
    def is_lit(self):
        return self.bouton_demarrer.is_active
                
                            
        