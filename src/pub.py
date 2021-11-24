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
        return drink in self.drinks

    def get_no_of_drinks(self):
        return len(self.drinks)

    def get_till(self):
        return self.till