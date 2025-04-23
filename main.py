from controler.controler import Controleur
import time
    
if __name__ == "__main__":
    try:
        app = Controleur()
        app.demarrer_thread()
        while True:
            time.sleep(1) #garde programme actif
        
    except Exception as e:
        print("Erreur de demarrage:", e)                               