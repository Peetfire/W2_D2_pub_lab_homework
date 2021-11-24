import unittest
import pdb
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    #@unittest.skip("delete...")
    def setUp(self):
        self.drink_1 = Drink("Monk IPA", 3.50, 4.7)
        self.drink_2 = Drink("Joker IPA", 3.60, 4.5)
        self.drink_3 = Drink("Camden Hells", 4.00, 3.9) 
        self.drinks = [self.drink_1, self.drink_2]
        self.customer = Customer("Dave", [], 20.00, 25)
        self.pub = Pub("The Prancing Pony", 100.00, self.drinks)

    #@unittest.skip("delete...")
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    #@unittest.skip("delete...")
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    # @unittest.skip("delete...")
    def test_pub_has_drinks(self):
        expected = self.drinks
        result = self.pub.drinks
        self.assertEqual(expected, result)

    # @unittest.skip("delete...")
    def test_add_drink(self):
        self.pub.add_drink(self.drink_3)  
        expected = 3
        result = self.pub.get_no_of_drinks()
        self.assertEqual(expected, result)

    # @unittest.skip("delete...")
    def test_remove_drink(self):
        self.pub.remove_drink(self.drink_2)
        expected = 1
        result = self.pub.get_no_of_drinks()
        self.assertAlmostEqual(expected, result)

    #@unittest.skip("delete...")
    def test_pub_can_increase_till(self):
        expected = 104
        self.pub.increase_till(4.00)
        result = self.pub.till
        self.assertEqual(expected, result)

    # @unittest.skip("delete...")
    def test_pub_has_drink(self):
        expected = True
        result = self.pub.has_drink(self.drink_2)
        self.assertEqual(expected, result)

    # @unittest.skip("delete...")
    def test_does_not_have_drink(self):
        expected = False
        result = self.pub.has_drink("bad name")
        self.assertEqual(expected, result)
    
    # @unittest.skip("delete...")
    #test with valid and invalid inputs
    def test_pub_get_number_of_drinks(self):
        expected = 2
        result = self.pub.get_no_of_drinks()
        self.assertEqual(expected, result)

    # @unittest.skip("delete...")
    #test with valid and invalid inputs
    def test_get_till(self):
        expected = 100
        result = self.pub.get_till()
        self.assertEqual(expected, result)


    # @unittest.skip("delete...")
    def test_sell_drink(self):
        self.pub.sell_drink(self.drink_2, self.customer)
        self.assertEqual(16.40, self.customer.get_wallet())
        self.assertEqual(1, self.customer.get_no_of_drinks())
        self.assertEqual(1,self.pub.get_no_of_drinks())
        self.assertEqual(103.60,self.pub.get_till())
        



    