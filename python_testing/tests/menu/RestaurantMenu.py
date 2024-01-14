class RestaurantMenu:
    def __init__(self):
        self.restaurants = {}

    def get_restaurant(self, restaurant_name):
        if restaurant_name not in self.restaurants:
            return f'Error: {restaurant_name} does not exist'
        return self.restaurants[restaurant_name]

    def add_restaurant(self, restaurant_name):
        if restaurant_name in self.restaurants:
            return f'Error: {restaurant_name} already exists'
        self.restaurants[restaurant_name] = {"menu": {}}
        return self

    def remove_restaurant(self, restaurant_name):
        if restaurant_name not in self.restaurants:
            return f'Error: {restaurant_name} does not exist'
        del self.restaurants[restaurant_name]
        return self

    def add_menu_item(self, restaurant_name, item_name, description, price):
        if price < 0:
            return 'Error: Price must be positive'
        if restaurant_name not in self.restaurants:
            return f'Error: {restaurant_name} does not exist'
        if item_name in self.restaurants[restaurant_name]['menu']:
            return f'Error: {restaurant_name} already has {item_name} in the menu'

        self.restaurants[restaurant_name]["menu"][item_name] = {"description": description, "price": price}
        return f"{item_name} added to {restaurant_name}' menu"

    def get_menu(self, restaurant_name):
        if restaurant_name not in self.restaurants:
            return f'Error: {restaurant_name} does not exist'
        
        menu = []
        for item_name, details in self.restaurants[restaurant_name]["menu"].items():
            menu.append({"name": item_name, "description": details["description"], "price": details["price"]})
        return menu

    def update_menu_item(self, restaurant_name, item_name, description, price):
        if price < 0:
            return 'Error: Price must be positive'
        if restaurant_name not in self.restaurants:
            return f'Error: {restaurant_name} does not exist'
        if item_name not in self.restaurants[restaurant_name]['menu']:
            return f'Error: {restaurant_name} does not have {item_name} in the menu'

        self.restaurants[restaurant_name]["menu"][item_name] = {"description": description, "price": price}
        return f"{item_name} updated in {restaurant_name}' menu"

    def delete_menu_item(self, restaurant_name, item_name):
        if restaurant_name not in self.restaurants:
            return f'Error: {restaurant_name} does not exist'
        if item_name not in self.restaurants[restaurant_name]['menu']:
            return f'Error: {restaurant_name} does not have {item_name} in the menu'

        del self.restaurants[restaurant_name]["menu"][item_name]
        return f"{item_name} removed from {restaurant_name}' menu"