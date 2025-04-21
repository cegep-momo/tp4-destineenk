from gpiozero import DistanceSensor
from time import sleep

capteur = DistanceSensor(echo = 12, trigger = 17, max_distance = 3)

while True:
    cm = capteur.distance * 100
    print("DIstance:"+ str(cm)+ "cm")
    sleep(1)