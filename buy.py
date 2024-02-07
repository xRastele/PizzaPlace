class Buy:
    def __init__(self, currency, restaurant_menu, pizza_factory):
        self.currency = currency
        self.restaurant_menu = restaurant_menu
        self.pizza_factory = pizza_factory

    def purchase_pizza(self, pizza_name):
        pizza = self.pizza_factory.create_pizza(pizza_name)
        if self.currency.subtract(pizza.currency_value):
            self.restaurant_menu.add_pizza(pizza_name)
            return True
        return False
