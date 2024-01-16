import pytest
from RestaurantMenu import RestaurantMenu
def test_delete_valid_menu_item():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")
    rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", 3.99)
    
    result = rg.delete_menu_item("Cafe Mocha", "Latte")
    
    assert result == "Latte removed from Cafe Mocha' menu"
    assert rg.get_menu("Cafe Mocha") == []

def test_delete_invalid_menu_item_nonexistent_restaurant():
    rg = RestaurantMenu()
    with pytest.raises(ValueError) as e:
        rg.delete_menu_item("Nonexistent Restaurant", "Burger")
    assert str(e.value) == "Error: Nonexistent Restaurant does not exist"

def test_delete_invalid_menu_item_nonexistent_item():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")

    with pytest.raises(ValueError) as e:
        rg.delete_menu_item("Cafe Mocha", "Latte")
    
    assert str(e.value) == "Error: Cafe Mocha does not have Latte in the menu"

def test_delete_invalid_menu_item_nonexistent_item_nonexistent_restaurant():
    rg = RestaurantMenu()

    with pytest.raises(ValueError) as e:
        rg.delete_menu_item("Nonexistent Restaurant", "Burger")
    
    assert str(e.value) == "Error: Nonexistent Restaurant does not exist"