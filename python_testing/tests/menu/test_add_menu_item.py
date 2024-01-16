import pytest
from RestaurantMenu import RestaurantMenu

def test_add_valid_menu_item():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")
    
    result = rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", 3.99)
    
    assert result == "Latte added to Cafe Mocha' menu"
    assert rg.get_menu("Cafe Mocha") == [{"name": "Latte", "description": "Smooth espresso with steamed milk", "price": 3.99}]

def test_add_invalid_menu_item_negative_price():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")

    with pytest.raises(ValueError) as e:
        rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", -1.99)
    
    assert str(e.value) == "Price must be positive"


def test_add_invalid_menu_item_nonexistent_restaurant():
    rg = RestaurantMenu()

    with pytest.raises(ValueError) as e:
        rg.add_menu_item("Nonexistent Restaurant", "Burger", "Delicious burger", 8.99)
    
    assert str(e.value) == "Error: Nonexistent Restaurant does not exist"

def test_add_invalid_menu_item_duplicate():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")
    rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", 3.99)

    with pytest.raises(ValueError) as e:
        rg.add_menu_item("Cafe Mocha", "Latte", "Another latte", 4.99)
    
    assert str(e.value) == "Cafe Mocha already has Latte in the menu"

#test invalid menu item duplicate
#*def test_add_invalid_menu_item_duplicate():
    #rg = RestaurantMenu()
    #rg.add_restaurant("Cafe Mocha")
    #rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", 3.99)

    #with pytest.raises(ValueError) as e:
        #rg.add_menu_item("Cafe Mocha", "Latte", "Another latte", 4.99)
    
    #assert str(e.value) == "Cafe Mocha already has Latte in the menu"