import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = None
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise Exception

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        return self.price with discount
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Get name
        """
        return f"{self.__name}"

    @name.setter
    def name(self, name: str) -> None:
        """
        Inout new name
        """
        self.__name = str(name).strip()[:10]

    @classmethod
    def instantiate_from_csv(cls, path_file: str) -> None:
        """
        Get csv file and create 5 classes
        """
        cls.all.clear()

        with open(path_file, 'r', encoding='windows-1251') as csv_file:
            file = csv.DictReader(csv_file)

            for row in file:
                cls(row['name'], float(row['price']), float(row['quantity']))

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Change from strint to float
        """
        clean_string = string.strip().replace(',', '.')
        return int(float(clean_string))