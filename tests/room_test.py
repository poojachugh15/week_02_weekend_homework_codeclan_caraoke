import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Senorita-Camila cabelle")
        self.song_2 = Song("Dance Monkey")
        self.song_3 = Song("Someone you loved")
        self.song_4 = Song("Memories-Maroon 5")
        self.song_5 = Song("Shape of you")
        self.room = Room("The CodeClan Caraoke", 900.00, 20.00)
        
        
    def test_room_has_name(self):
        self.assertEqual("The CodeClan Caraoke", self.room.name)
        
    def test_room_has_till(self):
        self.assertEqual(900.00, self.room.till)
        
    def test_room_can_add_song(self):
        self.room.add_songs(self.song_1)
        self.assertEqual(1, self.room.songs_count())
        
    def test_can_check_in_guest(self):
        guest = Guest("Mishti" , 400.00 )
        self.room.check_in(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_can_check_out_guest(self):
        guest = Guest("Mishti" , 400.00 )
        self.room.check_in(guest)
        self.room.check_out(guest)
        self.assertEqual(0, self.room.guest_count())
    
    def test_number_of_space(self):
        self.assertEqual(5, self.room.number_of_spaces)
        
    def test_room_has_entry_fee(self):
        self.assertEqual(20.00, self.room.entry_fee) 
        
    def test_room_has_one_guest(self):
        self.room.check_in_increase_amount(self.room)
        self.assertEqual(920.00, self.room.till)
        
    
       
       
       
       
       
       
       
       
       
       