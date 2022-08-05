import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Teenage Riot by Sonic Youth")
        self.song2 = Song("Human Fly by The Cramps")
        

    # set-up tests
    def test_song_has_name(self):
        self.assertEqual("Teenage Riot by Sonic Youth", self.song1.song_name)
