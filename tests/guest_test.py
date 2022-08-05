import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("The Great Waldo", 150)
        self.guest2 = Guest("Sandra the Voice of Reason", 60)

    # set-up tests
    def test_customer_has_name(self):
        self.assertEqual("The Great Waldo", self.guest1.guest_name)

    def test_customer_has_wallet(self):
        self.assertEqual(60, self.guest2.wallet)

    # function tests