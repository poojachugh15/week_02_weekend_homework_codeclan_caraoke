import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Mishti" , 400.00 )
        self.guest_2 = Guest("Eva" , 300.00)
        self.guest_3 = Guest("Sofia" , 500.00)
        self.guest_4 = Guest("Seina" , 200.00)
        self.guest_5 = Guest("Ryes" , 600.00)
        self.guest_6 = Guest("Craig" , 450.00)
        self.room = Room("The CodeClan Caraoke", 900.00, 20.00)
        
        
    def test_guest_has_name(self):
       self.assertEqual("Mishti", self.guest.name)
            
    def test_guest_has_wallet(self):
       self.assertEqual(400.00, self.guest.wallet)
        
    def test_guest_pay_entry_fee(self):
        self.guest.check_in_decrease_amount(self.room)
        self.assertEqual(380.00, self.guest.wallet)
      
    