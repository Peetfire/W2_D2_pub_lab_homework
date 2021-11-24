class Customer:
    def __init__(self, name, stomach, wallet, age, drunkenness):
        self.name = name
        self.stomach = stomach
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def get_wallet(self):
        return self.wallet

    def get_age(self):
        return self.age

    def get_drunkenness(self):
        return self.drunkenness

    def increase_drunkennes(self, amount):
        self.drunkenness += amount

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def add_drink(self, drink):
        self.stomach.append(drink)

    def buy_drink(self, drink):
        self.add_drink(drink)
        self.reduce_wallet(drink.price)
        self.increase_drunkennes(drink.abv)

    def get_no_of_drinks(self):
        return len(self.stomach)

