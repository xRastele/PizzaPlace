class Currency:
    def __init__(self):
        self.amount = 0

    def add(self, value):
        self.amount += value

    def subtract(self, value):
        if self.amount >= value:
            self.amount -= value
            return True
        return False

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
