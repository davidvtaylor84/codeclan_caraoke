import unittest

from src.drinks import Drinks
from src.guest import Guest
from src.room import Room

class TestDrinks(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drinks("Vodka Coke", 4.5)
        self.drink2 = Drinks("Leith Juice pint", 4.90)
        self.drink3 = Drinks("Large Glass Pinot Grigio", 4.90)

        # set-up tests
    def test_drinks_have_name(self):
        self.assertEqual("Vodka Coke", self.drink1.drink_name)

    def test_drinks_have_price(self):
        self.assertEqual(4.90, self.drink2.drink_price)

