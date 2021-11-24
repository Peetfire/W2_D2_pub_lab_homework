import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Monk IPA", 3.50, 4.7)

    def test_drink_has_name(self):
        result = self.drink.name
        expected = "Monk IPA"
        self.assertEqual(expected, result)

    def test_drink_has_price(self):
        result = self.drink.price
        expected = 3.50
        self.assertEqual(expected, result)

    def test_drink_has_abv(self):
        result = self.drink.abv
        expected = 4.7
        self.assertEqual(expected, result)          