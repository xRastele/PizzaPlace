import random


def generate_random_image_path():
    customer_images = ['assets/customer1.png', 'assets/customer2.png', 'assets/customer3.png',
                       'assets/customer4.png']

    random_image_path = random.choice(customer_images)
    return random_image_path


class Customer:
    def __init__(self, desired_pizza, img_path="assets/"):
        self.desired_pizza = desired_pizza
        self.reward = random.randint(20, 30)
        self.order_in_progress = False
        self.image_path = generate_random_image_path()
        self.is_order_completed = False
        print(self.image_path)

    def get_image_path(self):
        return self.image_path

    def place_order(self):
        self.order_in_progress = True

    def check_order_status(self):
        self.order_in_progress = False

    def notify(self):
        self.is_order_completed = True
