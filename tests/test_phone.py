from src.phone import Phone


def test_get_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 2)

    assert phone.number_of_sim == 2


def test_set_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 2)

    # Valid value
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3

    # Float value
    phone.number_of_sim = 1.5
    assert phone.number_of_sim == 3

    # Value is below zero
    phone.number_of_sim = -1
    assert phone.number_of_sim == 3

