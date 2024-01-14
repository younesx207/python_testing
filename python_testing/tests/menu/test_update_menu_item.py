import pytest
import RestaurantMenu
def test_update_valid_menu_item():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")
    rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", 3.99)

    result = rg.update_menu_item("Cafe Mocha", "Latte", "Creamy Latte", 4.99)

    assert result == "Latte updated in Cafe Mocha's menu"
    assert rg.get_menu("Cafe Mocha") == [{"name": "Latte", "description": "Creamy Latte", "price": 4.99}]

def test_update_invalid_menu_item_negative_price():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")
    rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", 3.99)

    with pytest.raises(ValueError) as e:
        rg.update_menu_item("Cafe Mocha", "Latte", "Creamy Latte", -1.99)
    
    assert str(e.value) == "Price must be positive"

def test_update_invalid_menu_item_nonexistent_restaurant():
    rg = RestaurantMenu()

    with pytest.raises(ValueError) as e:
        rg.update_menu_item("Nonexistent Restaurant", "Burger", "Delicious burger", 8.99)
    
    assert str(e.value) == "Error: Nonexistent Restaurant does not exist"

def test_update_invalid_menu_item_nonexistent_item():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")

    with pytest.raises(ValueError) as e:
        rg.update_menu_item("Cafe Mocha", "Latte", "Creamy Latte", 4.99)
    
    assert str(e.value) == "Error: Cafe Mocha does not have Latte in the menu"