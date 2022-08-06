import unittest

from src.bardrinks import BarDrinks
from src.guest import Guest
from src.room import Room

class TestBarDrinks:

    def setUp(self):
        self.room1 = Room("Red Room", 4, 50.00 )
        self.room2 = Room("Green Room", 6, 30.00)
        self.guest1 = Guest("Harry the Human Sub-Woofer", 90, "I Miss You by Blink 182")
        self.guest2 = Guest("Sylvia Skyshouter", 150, "Teenage Riot by Sonic Youth")
        self.guest3 = Guest("Jim Wildheart", 90, "Frack the Police by NWA")
        self.guest4 = Guest("Wanda Wanna Banana", 40, "Chimp Diaries by HelloWorld")
        self.guest5 = Guest("Kaneda", 70, "Venus in Furs by the Velvet Underground")
        self.bardrinks1 = BarDrinks("Vodka Coke", 4.5)
        self.bardrinks2 = BarDrinks("Leith Juice pint", 4.90)
        self.bardrinks3 = BarDrinks("Large Glass Pinot Grigio", 4.90)

        # set-up tests
    def test_drinks_have_name(self):
        self.assertequal("Vodka Coke", self.bardrinks1.drink_name)
