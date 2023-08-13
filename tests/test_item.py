"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_name1():
    return Item('name1', 12.34, 5)


def test_item_init(item_name1):
    assert item_name1.name == 'name1'
    assert item_name1.price == 12.34
    assert item_name1.quantity == 5


def test_item_calculate_total_price(item_name1):
    assert item_name1.calculate_total_price() == 61.7  # 12.34 * 5


def test_item_apply_discount(item_name1):
    Item.pay_rate = 0.5
    item_name1.apply_discount()
    assert item_name1.price == 6.17  # 12.34 * 0.5


def test_item_created_items_list():
    count = len(Item.all)
    name2 = Item('name2', 1, 1)
    assert len(Item.all) == count + 1
