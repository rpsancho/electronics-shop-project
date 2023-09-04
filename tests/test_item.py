"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


@pytest.fixture
def item_name1():
    return Item('name1', 12.34, 5)


@pytest.fixture
def item_class():
    return Item


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


def test_item_name_getter(item_name1):
    assert item_name1.name == 'name1'


def test_item_name_setter(item_name1):
    item_name1.name = '0123456789'
    assert item_name1.name == '0123456789'
    item_name1.name = '0123456789name1'
    assert item_name1.name == '0123456789'


def test_instantiate_from_csv(item_class):
    item_class.all = []
    assert len(item_class.all) == 0
    item_class.instantiate_from_csv()
    assert len(item_class.all) == 5

    item_class.CSV_PATH = '../tests/test_items111.csv'
    with pytest.raises(FileNotFoundError):
        item_class.instantiate_from_csv()

    item_class.CSV_PATH = '../tests/test_items.csv'
    with pytest.raises(InstantiateCSVError):
        item_class.instantiate_from_csv()


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item__repr__(item_name1):
    assert repr(item_name1) == "Item('name1', 12.34, 5)"


def test_item__str__(item_name1):
    assert str(item_name1) == 'name1'


def test_item__add__(item_name1):
    assert item_name1 + item_name1 == 10
    with pytest.raises(TypeError):
        5 + item_name1
