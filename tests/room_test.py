import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Red Room", 4, 50.00 )
        self.room2 = Room("Green Room", 6, 30.00)
        self.guest1 = Guest("Harry the Human Sub-Woofer", 90, "I Miss You by Blink 182")
        self.guest2 = Guest("Sylvia Skyshouter", 150, "Teenage Riot by Sonic Youth")
        self.guest3 = Guest("Jim Wildheart", 90, "Frack the Police by NWA")
        self.guest4 = Guest("Wanda Wanna Banana", 40, "Chimp Diaries by HelloWorld")
        self.guest5 = Guest("Kaneda", 70, "Venus in Furs by the Velvet Underground")
        self.song1 = Song("Wuthering Heights by Kate Bush")
        self.song2 = Song("4'33 by John Cage")

    # set-up tests
    def test_room_has_name(self):
        self.assertEqual("Red Room", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room2.room_capacity)

    def test_room_has_price(self):
        self.assertEqual(50.00, self.room1.room_price)

    # function tests
    def test_check_in_guests(self):
        add_guest = self.room1.check_in_guests(self.guest1.guest_name)
        self.assertEqual(["Harry the Human Sub-Woofer"], add_guest)

    def test_check_in_multiple_guests(self):
        add_guest1 = self.room1.check_in_guests(self.guest1.guest_name)
        add_guest2 = self.room1.check_in_guests(self.guest3.guest_name)
        self.assertEqual(["Harry the Human Sub-Woofer", "Jim Wildheart"], add_guest1, add_guest2)

    def test_check_out_guests(self):
        self.room2.check_in_guests(self.guest1.guest_name)
        self.room2.check_in_guests(self.guest2.guest_name)
        self.room2.check_in_guests(self.guest3.guest_name)
        removed_guests = self.room2.check_out_guests(self.guest3.guest_name)
        self.assertEqual(["Harry the Human Sub-Woofer", "Sylvia Skyshouter"], removed_guests)

    def test_add_song_to_room(self):
        add_song = self.room2.add_song_to_room(self.song1.song_name)
        self.assertEqual(["Wuthering Heights by Kate Bush"], add_song)

    def tests_add_multiple_songs(self):
        add_song1 = self.room2.add_song_to_room(self.song1.song_name)
        add_song2 = self.room2.add_song_to_room(self.song2.song_name)
        self.assertEqual(["Wuthering Heights by Kate Bush", "4'33 by John Cage"], add_song1, add_song2)

    def test_too_many_people_in_room(self):
        self.room1.check_in_guests(self.guest1.guest_name)
        self.room1.check_in_guests(self.guest2.guest_name)
        self.room1.check_in_guests(self.guest3.guest_name)
        self.room1.check_in_guests(self.guest4.guest_name)
        self.room1.check_in_guests(self.guest5.guest_name)
        capacity = self.room1.room_capacity_check(self.room1)
        self.assertEqual("ROOM CAPACITY EXCEEDED", capacity)

    def test_room_capacity_is_fine(self):
        self.room2.check_in_guests(self.guest1.guest_name)
        self.room2.check_in_guests(self.guest2.guest_name)
        self.room2.check_in_guests(self.guest3.guest_name)
        self.room2.check_in_guests(self.guest4.guest_name)            
        self.room2.check_in_guests(self.guest5.guest_name)
        capacity = self.room2.room_capacity_check(self.room2)
        self.assertEqual("Acceptable number of people in room. Sing away!", capacity)


