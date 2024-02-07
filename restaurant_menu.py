import inspect
import sys
from pizza import *


class RestaurantMenu:
    def __init__(self):
        self.available_pizzas = {cls.__name__: False for cls in Pizza.__subclasses__()}
        self.available_pizzas["MargheritaPizza"] = True

    def add_pizza(self, pizza_name):
        self.available_pizzas[pizza_name] = True

    def is_pizza_purchased(self, pizza_name):
        return self.available_pizzas.get(pizza_name, False)

    def get_available_pizzas(self):
        return self.available_pizzas

    def get_purchased_pizzas(self):
        purchased_pizzas = [pizza_name for pizza_name, purchased in self.available_pizzas.items() if purchased]
        return purchased_pizzas

    def clear_purchased_pizzas(self):
        self.available_pizzas = {cls.__name__: False for cls in Pizza.__subclasses__()}
        self.available_pizzas["MargheritaPizza"] = True
