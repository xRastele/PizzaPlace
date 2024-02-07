import inspect
import sys
import pygame


class Pizza:
    def __init__(self, name, clicks_required, currency_value, image_path='assets/'):
        self.name = name
        self.clicks_count = 0
        self.clicks_required = clicks_required
        self.currency_value = currency_value
        self.image_path = f'{image_path}{self.name}.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (150, 150))

        self.customer = None

    def set_customer(self, customer):
        self.customer = customer

    def add_pizza_click_count(self):
        self.clicks_count += 1
        if self.check_pizza_click_count():
            return True
        return False

    def check_pizza_click_count(self):
        if self.clicks_count >= self.clicks_required:
            self.clicks_count = 0
            if self.customer:
                self.customer.notify()
            self.customer = None
            return True


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("MargheritaPizza", 15, 15)


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("PepperoniPizza", 25, 30)


class FunghiPizza(Pizza):
    def __init__(self):
        super().__init__("FunghiPizza", 35, 50)


class OlivePizza(Pizza):
    def __init__(self):
        super().__init__("OlivePizza", 55, 75)


class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "MargheritaPizza":
            return MargheritaPizza()
        elif pizza_type == "PepperoniPizza":
            return PepperoniPizza()
        elif pizza_type == "FunghiPizza":
            return FunghiPizza()
        elif pizza_type == "OlivePizza":
            return OlivePizza()
        else:
            raise ValueError("Unknown pizza type")

    def get_all_pizza_classes(self):
        return [
            cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass)
            if issubclass(cls, Pizza) and cls is not Pizza
        ]

    def get_all_pizzas(self):
        pizza_classes = self.get_all_pizza_classes()
        pizzas = [pizza_class() for pizza_class in pizza_classes]
        return sorted(pizzas, key=lambda pizza: pizza.currency_value)
