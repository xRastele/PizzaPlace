import pygame
from button import Button
from commands import *
from pizza_shop_ui import PizzaShopUI

class GameUI:
    def __init__(self, surface, game):
        self.surface = surface
        self.game = game
        self.text_renderer = game.text_renderer
        self.restaurant_menu = game.restaurant_menu
        self.pizza_shop_ui = PizzaShopUI(game, self)
        self.current_pizza_name = None

        self.pizza_position_x = 100
        self.pizza_position_y = 465
        self.pizza_offset = 300

        self.save_command = SaveGameCommand()
        self.load_command = LoadGameCommand()

        self.buttons = [
            #Button(50, 650, 100, 50, "Upgrades", self.text_renderer, ShowUpgradesMenuCommand()),
            Button(160, 650, 100, 50, "Save", self.text_renderer, self.save_command),
            Button(270, 650, 100, 50, "Load", self.text_renderer, self.load_command),
            Button(380, 650, 100, 50, "Pizzas", self.text_renderer, ShowPizzasMenuCommand(self.pizza_shop_ui))
        ]

        #Add pizzas to the counter available from the start
        self.add_pizzas_to_counter()

    def add_pizzas_to_counter(self):
        purchased_pizzas = self.game.restaurant_menu.get_purchased_pizzas()

        for pizza_name in purchased_pizzas:
            if pizza_name not in self.game.pizzas_on_counter:
                pizza_obj = self.game.pizza_factory.create_pizza(pizza_name)
                self.game.pizzas_on_counter[pizza_name] = pizza_obj

    def draw_pizzas_and_click_counter(self):
        x, y = self.pizza_position_x, self.pizza_position_y
        for pizza_name, pizza_obj in self.game.pizzas_on_counter.items():
            self.surface.blit(pizza_obj.image, (x, y))
            #Render text - click count
            self.text_renderer.render(self.surface, f"{pizza_obj.clicks_count+1}/{pizza_obj.clicks_required}", (x-15,y))
            x += self.pizza_offset

    def draw(self):
        #Draw pizzas on counter
        self.draw_pizzas_and_click_counter()

        #Draw currency box, currency text
        currency_text = f"Currency: {self.game.currency.get_amount()}"
        OFFSET_PX = 5
        self.text_renderer.render(self.surface, currency_text, (20 + OFFSET_PX, 20 + OFFSET_PX))

        #Draw buttons
        for button in self.buttons:
            button.draw(self.surface)

        #Draw pizza shop menu
        self.pizza_shop_ui.draw(self.surface)

    def handle_click(self, pos):
        for button in self.buttons:
            if button.is_clicked(pos) and button.command:
                if button.command == self.save_command:
                    self.save_game()
                elif button.command == self.load_command:
                    self.load_game()
                else:
                    button.command.execute()

        if self.pizza_shop_ui.visible:
            self.pizza_shop_ui.handle_click(pos)

        if not self.pizza_shop_ui.visible:
            self.handle_pizza_click(pos)

    def handle_pizza_click(self, pos):
        x, y = self.pizza_position_x, self.pizza_position_y
        for pizza_name, pizza_obj in self.game.pizzas_on_counter.items():
            pizza_rect = pygame.Rect(x, y, pizza_obj.image.get_width(), pizza_obj.image.get_height())
            if pizza_rect.collidepoint(pos):
                self.current_pizza_name = pizza_name
                if pizza_obj.add_pizza_click_count():
                    if self.game.current_customer and self.game.current_customer.desired_pizza == pizza_name:
                        self
                    self.game.currency.add(pizza_obj.currency_value)
                break
            x += self.pizza_offset

    def save_game(self):
        game_state = self.game.create_memento()
        self.save_command.execute(game_state)
        print("Game saved")

    def load_game(self):
        game_state = self.load_command.execute()
        if game_state:
            self.game.set_memento(game_state)
            for pizza_name in game_state.purchased_pizzas:
                self.restaurant_menu.add_pizza(pizza_name)
            self.add_pizzas_to_counter()
            self.draw_pizzas_and_click_counter()
            print("Game loaded")