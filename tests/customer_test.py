import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Mr Smith", [], 10.00, 19)
        self.customer_2 = Customer("Basil Brush", [], 100.00, 18)
        self.customer_3 = Customer("Jimmy Cranky", [], 5.00, 17)

    #@unittest.skip("delete...")
    def test_customer_has_name(self):
        result = self.customer.name
        expected = "Mr Smith"
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_customer_has_stomach(self):
        result = self.customer.stomach
        expected = []
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_customer_has_wallet(self):
        result = self.customer.wallet
        expected = 10.00
        self.assertEqual(expected, result)

    def test_customer_has_age(self):
        result = self.customer.age
        expected = 19
        self.assertEqual(expected, result)        

    #@unittest.skip("delete...")
    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3.50)
        result = self.customer.wallet
        expected = 6.50
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_add_drink(self):
        drink_1 = Drink("IPA", 5.10, 4.00)
        self.customer.add_drink(drink_1)
        result = 1
        expected = len(self.customer.stomach)
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_get_number_of_drinks(self):
        result = 0
        expected = self.customer.get_no_of_drinks()
        self.assertEqual(expected, result)

    

    

    

    
