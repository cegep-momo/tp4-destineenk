from gpiozero import Button
from time import sleep

# Création des objets pour chaque bouton avec pull-down
bouton_start = Button(23) # Résistance pull-down pour GPIO 23
bouton_mesure = Button(24)  # Résistance pull-down pour GPIO 24


# Associer les actions aux boutons

# Boucle principale pour tester
while True:
    if bouton_start.is_pressed:
        print("fonctionne")
    elif bouton_mesure.is_pressed:
        print("ok")
    sleep(1)  # Attend une seconde pour vérifier si les boutons sont pressés

