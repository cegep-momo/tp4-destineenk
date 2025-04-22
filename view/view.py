import LCD1602
from time import sleep

class Vue:
    def __init__(self):
        self.lcd = LCD1602
        self.lcd.init(0x27, 1)
        
    def affichage_ecran(self, rangee1="", rangee2=""):
        self.lcd.clear()
        self.lcd.write(0,0, rangee1[:16])
        self.lcd.write(0,1, rangee2[:16])
        

    def message_activation(self):
         self.affichage_ecran("Systeme actif")
    
    def message_arret(self):
        self.affichage_ecran("Systeme arrete")
    
    def message_mesure(self):
         self.affichage_ecran("Mesure active")
         
    def desactivation_mesure(self):
        self.lcd.clear()
    
    def message_distance(self, distance_mesure):
        self.affichage_ecran(f"Distance: {distance_mesure} cm")
