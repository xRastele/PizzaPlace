import pickle

class Command:
    def execute(self):
        pass

class SaveGameCommand(Command):
    def execute(self, game_state):
        with open("save_file.pickle", "wb") as file:
            pickle.dump(game_state, file)

class LoadGameCommand(Command):
    def execute(self):
        try:
            with open("save_file.pickle", "rb") as file:
                game_state = pickle.load(file)
            return game_state
        except FileNotFoundError:
            print("Save file not found")
            return None

class ShowUpgradesMenuCommand(Command):
    def execute(self):
        print("Upgrade menu")

class ShowPizzasMenuCommand(Command):
    def __init__(self, pizza_shop_ui):
        self.pizza_shop_ui = pizza_shop_ui
    def execute(self):
        self.pizza_shop_ui.toggle_visibility()
        print("Pizzas menu")

class PurchasePizzaCommand(Command):
    def __init__(self, pizza_name, buy_process, game_ui):
        self.pizza_name = pizza_name
        self.buy_process = buy_process
        self.game_ui = game_ui

    def execute(self):
        if self.buy_process.purchase_pizza(self.pizza_name):
            self.game_ui.add_pizzas_to_counter()
            return True
        return False
