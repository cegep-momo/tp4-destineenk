import json, codecs
from moduleTP4 import Mesure

class Modele:
    def __init__(self, fichier):
        self.fichier = fichier
        self.mesures = []
        
    def creer_mesure(self, distance):
        mesure = Mesure(distance)
        self.mesures.append(mesure)
        
    def enregister_donnees(self):
        nouvelles_donnees = []
        for mesure in self.mesures:
            nouvelles_donnees.append(mesure.afficherMesure())
      
        try:
            with codecs.open(self.fichier,  "r", encoding="utf-8") as f:
                donnees = json.load(f)
                
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erreur lors de louverture du fichier: {e}")
            donnees = []
            
        donnees.append(nouvelles_donnees)
        
        with codecs.open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent= 4, ensure_ascii = False)
            print(f"Donnees enregistrées dans {self.fichier}: {donnees}")  # Vérifie le contenu du fichier
