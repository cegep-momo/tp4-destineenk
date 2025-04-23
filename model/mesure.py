import json, codecs
import os
import datetime


class Mesure:
    def __init__(self, distance):
        self.dateHeureMesure = datetime.datetime.now()
        self.dataMesure = distance
        self.fichier = "donnees.json"
        
    def __repr__(self):
        return  f"Mesure(date= {self.dateHeureMesure}, distance={self.dataMesure})"
    
    def afficherMesure(self):
        return  f"Date et heure {self.dateHeureMesure}, Donnee mesuree: {self.dataMesure}"

    

    def sauvegarderJson(self):
        print(os.path.curdir)
        if os.path.exists(self.fichier):
            try:
                with open(self.fichier, encoding="utf-8") as fichier:
                    data = json.load(fichier)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Erreur lors de la lecture du fichier")
                data = {"donnees": []}
        
                
        mesures_dict = {
        "Date et heure": str(self.dateHeureMesure),
        "Donnee mesuree": str(self.dataMesure)
        }
        data["donnees"].append(mesures_dict)
         
            
        
        with codecs.open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii = False,
            indent=4, sort_keys=True)
