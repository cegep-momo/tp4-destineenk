from gpiozero import DistanceSensor
from time import sleep

capteur = DistanceSensor(echo=12, trigger=17, max_distance=3)

while True:
    distance_cm = capteur.distance * 100
    print(f"Distance: {distance_cm:.1f} cm")
    sleep(1)
