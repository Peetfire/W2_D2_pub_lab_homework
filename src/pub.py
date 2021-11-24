class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_drink(self, new_drinks):
        self.drinks.extend(new_drinks)

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

    def sell_drink(self, drink, customer):
        self.increase_till(drink.price)
