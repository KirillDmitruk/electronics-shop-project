import pytest

from src.item import Item
from src.keyboard import Keyboard, Mixin


@pytest.fixture
def fixture_class():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    return keyboard


def test_class(fixture_class):
    assert isinstance(fixture_class, object)
    assert issubclass(Keyboard, Item)
    assert issubclass(Keyboard, Mixin)
    assert str(fixture_class) == "Dark Proje"


def test_lang_in_keyboard(fixture_class):
    assert fixture_class.language == 'EN'

    fixture_class.change_lang()
    assert fixture_class.language == 'RU'

    fixture_class.change_lang()
    assert fixture_class.language == 'EN'
    #
    # fixture_class.language = 'CH'