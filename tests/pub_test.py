import unittest
import pdb
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    #@unittest.skip("delete...")
    def setUp(self):
        drink_1 = Drink("Monk IPA", 3.50, 4.7)
        drink_2 = Drink("Joker IPA", 3.60, 4.5)
        drink_3 = Drink("Camden Hells", 4.00, 3.9) 
        drinks = [drink_1, drink_2, drink_3]
        customer = Customer("Dave", [], 20.00)
        self.pub = Pub("The Prancing Pony", 100.00, drinks)

    #@unittest.skip("delete...")
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    #@unittest.skip("delete...")
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    @unittest.skip("delete...")
    def test_pub_has_drinks(self):
        drink_1 = Drink("Monk IPA", 3.50, 4.7)
        drink_2 = Drink("Joker IPA", 3.60, 4.5)
        drink_3 = Drink("Camden Hells", 4.00, 3.9) 
        drinks = [drink_1, drink_2, drink_3]
        expected = drinks
        result = self.pub.drinks
        self.assertEqual(expected, result)

    @unittest.skip("delete...")
    def test_add_drink(self):
        drink_1 = Drink("Monk IPA", 3.50, 4.7)
        drink_2 = Drink("Joker IPA", 3.60, 4.5)
        drink_3 = Drink("Camden Hells", 4.00, 3.9) 
        drinks = [drink_1, drink_2, drink_3]
        self.pub.add_drink(drinks)  
        expected = drinks 
        result = self.pub.drinks
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_pub_can_increase_till(self):
        expected = 104
        self.pub.increase_till(4.00)
        result = self.pub.till
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_pub_has_drink(self):
        expected = Drink("Joker IPA", 3.60, 4.5).name
        result = self.pub.has_drink("Joker IPA").name
        self.assertEqual(expected, result)

    @unittest.skip("delete...")
    def test_does_not_have_drink(self):
        expected = True
        result = self.pub.has_drink("bad name")
        self.assertEqual(expected, result)

    @unittest.skip("delete...")
    #test with valid and invalid inputs
    def test_can_choose_drink(self):
        expected = drink_1
        result = self.pub.choose_drink()
        self.assertEqual(expected, result)
    
    @unittest.skip("delete...")
    #test with valid and invalid inputs
    def test_pub_get_number_of_drinks(self):
        expected = 3
        result = self.pub.get_drinks()
        self.assertEqual(expected, result)

    @unittest.skip("delete...")
    #test with valid and invalid inputs
    def test_get_till(self):
        expected = 100
        result = self.pub.get_till()
        self.assertEqual(expected, result)


    @unittest.skip("delete...")
    def test_sell_drink(self):
        self.pub.sell_drink(drink_2, customer)
        self.assertEqual(16.40, customer.get_wallet())
        self.assertEqual(1, customer.get_number_of_drinks())
        self.assertEqual(2,pub.get_number_of_drinks())
        self.assertEqual(103.60,pub.get_till())
        



    