import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from src.f4 import cls_inventory

import pytest

@pytest.fixture
def no_stock_inventory():
    """Returns an empty inventory that can store 100 items"""
    return cls_inventory(100)

def test_buy_and_sell_nikes_adidas(no_stock_inventory):

    # Create inventory object
    inventory = no_stock_inventory
    assert inventory.limit == 100
    assert inventory.total_items == 0

    # Add the new Nike sneakers
    inventory.add_new_stock("Nike Sneakers", 50.00, 10)
    assert inventory.total_items == 10

    # Add the new Adidas sweatpants
    inventory.add_new_stock("Adidas Sweatpants", 70.00, 5)
    assert inventory.total_items == 15

    # Remove 2 sneakers to sell to the first customer
    inventory.remove_stock("Nike Sneakers", 2)
    assert inventory.total_items == 13

    # Remove 1 sweatpants to sell to the next customer
    inventory.remove_stock("Adidas Sweatpants", 1)
    assert inventory.total_items == 12
