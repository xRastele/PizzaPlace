import pygame
from commands import PurchasePizzaCommand
from button import Button
from utils import format_pizza_name


class PizzaShopUI:
    def __init__(self, game, game_ui):
        self.game = game
        self.game_ui = game_ui
        self.visible = False
        self.menu_rect = pygame.Rect(100, 100, 300, 400)
        self.pizzas = game.pizza_factory.get_all_pizzas()
        self.coin_image = pygame.image.load('assets/gold_coin.png')
        self.coin_image = pygame.transform.scale(self.coin_image, (25, 25))
        self.restaurant_menu = game.restaurant_menu
        self.purchase_buttons = {}

    def toggle_visibility(self):
        self.visible = not self.visible

        if not self.visible:
            self.clear_menu_area()

    def draw(self, surface):
        if not self.visible:
            return

        pygame.draw.rect(surface, (200, 200, 200), self.menu_rect)
        coin_width, coin_height = self.coin_image.get_size()

        for i, pizza in enumerate(self.pizzas):
            formatted_name = format_pizza_name(pizza.name)
            if self.restaurant_menu.is_pizza_purchased(pizza.name):
                text = f"{formatted_name} - Purchased"
            else:
                text = f"{formatted_name} - {pizza.currency_value}"

            text_surface = self.game.text_renderer.font.render(text, True, (0, 0, 0))
            text_width, text_height = self.game.text_renderer.font.size(text)

            text_x = self.menu_rect.x + 10
            text_y = self.menu_rect.y + 30 * i + 10

            surface.blit(text_surface, (text_x, text_y))

            if not self.restaurant_menu.is_pizza_purchased(pizza.name):
                coin_x = text_x + text_width + 5
                coin_y = text_y - 5

                button_x = coin_x + coin_width + 5
                button_y = text_y - 2

                surface.blit(self.coin_image, (coin_x, coin_y))
                purchase_command = PurchasePizzaCommand(pizza.name, self.game.buy_process, self.game_ui)
                purchase_button = Button(button_x, button_y, 60, 20, "Buy", self.game.text_renderer,
                                         purchase_command)
                self.purchase_buttons[pizza.name] = purchase_button
                purchase_button.draw(surface)

    def update_purchase_buttons(self, pizza_name, button):
        self.purchase_buttons.pop(pizza_name)
        self.game_ui.draw()

    def clear_menu_area(self):
        background_color = (0, 0, 0)
        self.game.surface.fill(background_color, self.menu_rect)

    def handle_click(self, pos):
        for pizza_name, button in self.purchase_buttons.items():
            if button.is_clicked(pos):
                if button.command.execute():
                    self.update_purchase_buttons(pizza_name, button)
                    break
