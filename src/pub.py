class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.is_drunk = 40.00

    def add_drink(self, new_drinks):
        self.drinks.append(new_drinks)

    def remove_drink(self, drink):
        if drink in self.drinks:
            self.drinks.remove(drink)

    def increase_till(self, amount):
        self.till += amount

    def has_drink(self, drink):
        return drink in self.drinks

    def get_no_of_drinks(self):
        return len(self.drinks)

    def get_till(self):
        return self.till

    def check_over_age(self, customer):
        return customer.age >= 18

    def check_is_drunk(self, customer):
        return customer.drunkenness > self.is_drunk

    def sell_drink(self, drink, customer):
        if self.check_over_age(customer) and not self.check_is_drunk(customer):
            self.increase_till(drink.price)
            self.remove_drink(drink)
            customer.buy_drink(drink)

