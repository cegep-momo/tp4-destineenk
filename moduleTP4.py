import datetime


class Mesure:
    def __init__(self, distance):
        self.dateHeureMesure = datetime.datetime.now()
        self.dataMesure = distance
        
    def __repr__(self):
        return str(self.dateHeureMesure, self.dataMesure)
    
    def afficherMesure(self):
        affichage_distance = {
            "dateHeureMesure": str(self.dateHeureMesure),
            "dataMesure": str(self.dataMesure)
        }
        
        return affichage_distance
