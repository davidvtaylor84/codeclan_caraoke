import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("The Great Waldo", 40, "I Miss You by Blink 182")
        self.guest2 = Guest("Sandra the Voice of Reason", 60, "Teenage Riot by Sonic Youth")
        self.room1 = Room("Red Room", 4, 50.00 )
        self.song1 = Song("I Miss You by Blink 182")
        self.song2 = Song("Song 2 by Blur")
        self.song3 = Song("Red Right Hand by Nick Cave")

    # set-up tests
    def test_customer_has_name(self):
        self.assertEqual("The Great Waldo", self.guest1.guest_name)

    def test_customer_has_wallet(self):
        self.assertEqual(60, self.guest2.wallet)

    # function tests

    def test_pay_for_room(self):
        self.guest2.pay_for_room(self.room1, self.guest2)
        self.assertEqual(10, self.guest2.wallet)

    def test_cannot_pay_for_room(self):
        no_money = self.guest1.pay_for_room(self.room1, self.guest1)
        self.assertEqual("You don't have enough money", no_money)

    def test_favourite_song(self):
        self.room1.add_song_to_room(self.song1.song_name)
        fav_song = self.guest1.my_favourite_song(self.room1, self.guest1)
        self.assertEqual("Yes! This is my jam!", fav_song)

    def test_favourite_song_in_larger_list(self):
        self.room1.add_song_to_room(self.song1.song_name)
        self.room1.add_song_to_room(self.song2.song_name)
        self.room1.add_song_to_room(self.song3.song_name)
        fav_song = self.guest1.my_favourite_song(self.room1, self.guest1)
        self.assertEqual("Yes! This is my jam!", fav_song)

    def test_song_not_in_list(self):
        self.room1.add_song_to_room(self.song1.song_name)
        self.room1.add_song_to_room(self.song2.song_name)
        self.room1.add_song_to_room(self.song3.song_name)
        fav_song = self.guest2.my_favourite_song(self.room1, self.guest2)
        self.assertEqual("Meh..", fav_song)

