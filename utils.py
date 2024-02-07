def format_pizza_name(pizza_class_name):
    if pizza_class_name.endswith("Pizza"):
        return pizza_class_name[:-5]
    return pizza_class_name