import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Red Room", 12, 50.00 )
        self.room2 = Room("Green Room", 6, 30.00)

    # set-up tests
    def test_room_has_name(self):
        self.assertEqual("Red Room", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room2.room_capacity)

    def test_room_has_price(self):
        self.assertEqual(50.00, self.room1.room_price)

    # function tests