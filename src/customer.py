class Customer:
    def __init__(self, name, stomach, wallet):
        self.name = name
        self.stomach = stomach
        self.wallet = wallet

    def get_wallet(self):
        return self.wallet

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def add_drink(self, drink):
        self.stomach.append(drink)

    def get_no_of_drinks(self):
        return len(self.stomach)

