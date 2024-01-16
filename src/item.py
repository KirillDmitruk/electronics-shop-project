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
        return (f"{self.__name} privat name\n"
                f"{self.name} not privat name\n"
                f"P{self.price} price\n"
                f"{self.quantity} quantity\n"
                f"{self.all} all items\n")

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
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name


    @classmethod
    def instantiate_from_csv(cls, filename='src/items.csv'):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        cls.all.clear()
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                Item.all.append(Item(row['name'], row['price'], row['quantity']))


    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Change from strint to float
        """
        clean_string = string.strip().replace(',', '.')
        return int(float(clean_string))
