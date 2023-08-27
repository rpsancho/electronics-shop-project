import pytest
from src.phone import Phone


@pytest.fixture
def phone_name():
    return Phone('phone_name', 57000.1, 6, 2)


def test_phone_init(phone_name):
    assert phone_name.name == 'phone_name'
    assert phone_name.price == 57000.1
    assert phone_name.quantity == 6
    assert phone_name.number_of_sim == 2


def test_phone_number_of_sim(phone_name):
    with pytest.raises(ValueError):
        phone_name.number_of_sim = 0
    with pytest.raises(ValueError):
        phone_name.number_of_sim = 1.1
    with pytest.raises(ValueError):
        phone_name.number_of_sim = -1
    phone_name.number_of_sim = 3
    assert phone_name.number_of_sim == 3


def test_phone__repr__(phone_name):
    assert repr(phone_name) == "Phone('phone_name', 57000.1, 6, 2)"


def test_phone__str__(phone_name):
    assert str(phone_name) == 'phone_name'


def test_phone__add__(phone_name):
    assert phone_name + phone_name == 12
    with pytest.raises(TypeError):
        6 + phone_name
