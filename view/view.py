import LCD1602
import time

class Vue:
    def __init__(self):
        self.lcd = LCD1602
        self.lcd.init(0x27, 1)

    def message_activation(self):
         self.lcd.write(0,0, "Systeme actif")
         self.lcd.write(1,1, "      ")  
    
    def message_arret(self):
        self.lcd.write(0,0, "Systeme arrete")
        self.lcd.write(1,1, "     ")
    
    def message_mesure(self):
         self.lcd.write(0,0, "Mesure active")
         self.lcd.write(1,1, "          ")
    
    def message_distance(self, distance_mesure):
        self.lcd.write(0,0, "Distance     ")
        self.lcd.write(1,1, f"{distance_mesure} cm")