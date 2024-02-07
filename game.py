from currency import Currency
from pizza import PizzaFactory
from text_renderer import TextRenderer
from restaurant_menu import RestaurantMenu
from game_state import GameState
from buy import Buy
from customer import Customer
import pygame
import settings
import random

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.currency = Currency()
        self.pizza_factory = PizzaFactory()
        self.text_renderer = TextRenderer()
        self.restaurant_menu = RestaurantMenu()
        self.buy_process = Buy(self.currency, self.restaurant_menu, self.pizza_factory)

        self.pizzas_on_counter = {}

        self.background_image = pygame.image.load('assets/background.png')
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

        self.current_customer = None
        self.customers = []

    def generate_customer(self):
        if not self.current_customer:
            desired_pizza = random.choice(list(self.restaurant_menu.get_purchased_pizzas()))
            customer = Customer(desired_pizza)
            self.customers.append(customer)
            self.current_customer = customer

    def serve_customers(self):
        if self.current_customer:
            if self.current_customer.desired_pizza in self.pizzas_on_counter:

                pizza_obj = self.pizzas_on_counter[self.current_customer.desired_pizza]

                pizza_obj.set_customer(self.current_customer)
            if self.current_customer.is_order_completed:
                self.currency.add(self.current_customer.reward)
                self.current_customer = None

    def update(self):
        if pygame.time.get_ticks() % 400 == 0:
            self.generate_customer()
        self.serve_customers()

    def draw(self):
        self.surface.blit(self.background_image, (0, 0))
        if self.current_customer:
            customer_image = pygame.image.load(self.current_customer.get_image_path())
            customer_image = pygame.transform.scale(customer_image,(250,345))
            self.surface.blit(customer_image, (settings.SCREEN_WIDTH/2 - 125, settings.SCREEN_HEIGHT/2 - 253))

            pizza_image = pygame.image.load(f'assets/{self.current_customer.desired_pizza}.png')
            pizza_image = pygame.transform.scale(pizza_image,(125,125))
            self.surface.blit(pizza_image, (settings.SCREEN_WIDTH/2-60, settings.SCREEN_HEIGHT/8 - 65))
        pass

    def create_pizza(self, pizza_type):
        return self.pizza_factory.create_pizza(pizza_type)

    def get_currency_amount(self):
        return self.currency.get_amount()

    def create_memento(self):
        purchased_pizzas = list(self.restaurant_menu.get_purchased_pizzas())
        pizza_objects = {pizza_name: pizza for pizza_name, pizza in self.pizzas_on_counter.items()}
        return GameState(self.currency.get_amount(), purchased_pizzas, pizza_objects)

    def set_memento(self, game_state):
        self.currency.set_amount(game_state.currency_amount)

        self.restaurant_menu.clear_purchased_pizzas()
        self.pizzas_on_counter.clear()

        for pizza_name in game_state.purchased_pizzas:
            self.restaurant_menu.add_pizza(pizza_name)
