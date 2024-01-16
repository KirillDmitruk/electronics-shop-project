"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def item_fixture():
    return Item('Смартфон', 10000, 20)


def test_item_init(item_fixture):
    assert item_fixture.name == "Смартфон"
    assert item_fixture.price == 10000
    assert item_fixture.quantity == 20


def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 200000


def test_apply_discount(item_fixture):
    Item.pay_rate = 0.8
    item_fixture.apply_discount()
    assert item_fixture.price == 8000.0








