import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('keyboard_name', 1200.1, 22)


def test_keyboard_init(keyboard1):
    assert keyboard1.name == 'keyboard_name'
    assert keyboard1.price == 1200.1
    assert keyboard1.quantity == 22
    assert keyboard1.language == 'EN'


def test_keyboard_language(keyboard1):
    with pytest.raises(AttributeError):
        keyboard1.language = 'CH'
    assert keyboard1.language == 'EN'
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang().change_lang()
    assert keyboard1.language == 'RU'
