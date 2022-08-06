import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("The Great Waldo", 40)
        self.guest2 = Guest("Sandra the Voice of Reason", 60)
        self.room1 = Room("Red Room", 4, 50.00 )

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