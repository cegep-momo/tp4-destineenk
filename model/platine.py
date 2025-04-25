from gpiozero import Button, DistanceSensor
from time import sleep
from view.view import Vue
from time import sleep
from view.view import Vue
from model.mesure import Mesure

class Platine:
    def __init__(self):
       #ininialisation des variables
        self.systeme_demarrer = False # systeme en marche
        self.mesure = False #systeme de mesure en marche
        self.capteur = DistanceSensor(echo = 16, trigger = 17) #capteur de distance
        self.vue = Vue() 
        self.liste_mesure = [] #donnees mesurees sous forme de liste
        self.bouton_demarrer = Button(23) #bouton pour demarrer le syteme
        self.bouton_mesure = Button(24) #bouton pour prendre les mesures
    
    def lire_valeurs(self):
          while True:
            if self.bouton_demarrer.is_pressed: #si le bouton demarre est appuye
                self.systeme_demarrer = not self.systeme_demarrer #le systeme devient actif
                if self.systeme_demarrer:
                    self.vue.message_activation()   #on affiche le message "Systeme actif sur lecran"                      
                else:
                    self.arreter_lecture() #lorsque on appuie une deuxiem fois, on affiche le message "systeme arrete" et appel la methode pour arreter le systeme
                    #explication de la methode plus bas
                sleep(1)
                
            if self.systeme_demarrer and self.bouton_mesure.is_pressed: #si le systeme est actif et quon appuie sur le bouton mesure
                self.vue.message_mesure() #on affiche le message mesure active sur lecran
                self.mesure = True # on active la prise de mesure
                sleep(1)
                while self.bouton_mesure.is_pressed:
                    sleep(0.1)
                
            if self.systeme_demarrer and self.mesure: #si le systeme est demarre et la prise de me sure est active aussi
                self.cm = round(self.capteur.distance * 100, 2) #on peut tester la distance s
                self.vue.message_distance(self.cm) #elle sera affichee avec 2 chiffres apres la virgule sur lecran
                self.liste_mesure.append(self.cm) #enregistre sous forme de liste
                sleep(5)
                
    def arreter_lecture(self):
        self.vue.message_arret() #on affiche le message "systeme arrete"
        sleep(1)
        self.mesure = False #desactive la prise de mesure
        self.vue.desactivation_mesure() #efface lecran
        print("Sauvegarde des mesures") #
        for distance in self.liste_mesure: #on enregistre tous les distances stockees dans liste mesurees dans le fichier json
            mesure = Mesure(distance) 
            mesure.sauvegarderJson() 
        print("Sauvegarde terminee")
        
   
    def get_liste_mesure(self):
        return self.liste_mesure #liste des distances mesurees
    
        
    def is_lit(self):
        return self.bouton_demarrer.is_active #methode utilisee pour les tests unitaires
                
                            
        