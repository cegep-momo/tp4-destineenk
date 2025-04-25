import unittest 
from gpiozero.pins.mock import MockFactory
from gpiozero import Device
from model.platine import Platine

#Configure gpiozero pour utiliser le simulateur
Device.pin_factory = MockFactory()

class Tester(unittest.TestCase):
    def setUp(self):
        self.platine = Platine()
    
    def test_bouton_appuye(self):
        self.platine.bouton_demarrer.pin.drive_low()
        self.assertTrue(self.platine.is_lit())
        
 
    def test_bouton_relache(self):
        self.platine.bouton_demarrer.pin.drive_high()
        self.assertFalse(self.platine.is_lit())


    
if __name__ == "__main__":
    unittest.main()