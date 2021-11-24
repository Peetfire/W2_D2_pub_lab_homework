class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_drink(self, new_drinks):
        self.drinks += new_drinks

    def increase_till(self, amount):
        self.till += amount

    def has_drink(self, drink):
        if drink in self.drinks:
            return drink