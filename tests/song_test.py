import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("song_1")
        self.song_1 = Song("Senorita-Camila cabelle")
        self.song_2 = Song("Dance Monkey")
        self.song_3 = Song("Someone you loved")
        self.song_4 = Song("Memories-Maroon 5")
        self.song_5 = Song("Shape of you")
        
    def test_song_by_name(self):
        self.assertEqual("Senorita-Camila cabelle", self.song_1.name)
                                          
      