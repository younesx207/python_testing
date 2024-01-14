import pytest
import RestaurantMenu
def test_get_menu_valid():
    rg = RestaurantMenu()
    rg.add_restaurant("Cafe Mocha")
    rg.add_menu_item("Cafe Mocha", "Latte", "Smooth espresso with steamed milk", 3.99)
    rg.add_menu_item("Cafe Mocha", "Cappuccino", "Espresso with frothy milk", 4.99)

    result = rg.get_menu("Cafe Mocha")

    assert result == [
        {"name": "Latte", "description": "Smooth espresso with steamed milk", "price": 3.99},
        {"name": "Cappuccino", "description": "Espresso with frothy milk", "price": 4.99}
    ]

def test_get_menu_invalid_nonexistent_restaurant():
    rg = RestaurantMenu()

    with pytest.raises(ValueError) as e:
        rg.get_menu("Nonexistent Restaurant")
    
    assert str(e.value) == "Error: Nonexistent Restaurant does not exist"