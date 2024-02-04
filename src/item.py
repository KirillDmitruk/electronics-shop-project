import csv
from pathlib import Path
import os

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    PATH_CSV = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "src", "items.csv")


    @property
    def name(self):
        """
        Возвращает приватное имя
        """
        return self.__name


    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            print('Длина наименования товара превышает 10 символов.')
            self.__name = value[:10]



    @classmethod
    def instantiate_from_csv(cls, filename: str | None = PATH_CSV) -> None:
        """
        Инициализирует экземпляры класса данными из файла csv
        """
        cls.all.clear()
        try:
            with open(filename, newline="",
                      encoding="windows-1251'", errors="replace") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row["name"]
                    price = int(row["price"])
                    quantity = int(row["quantity"])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except Exception:
            raise InstantiateCSVError


    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        clean_string = string.strip().replace(',', '.')
        return int(float(clean_string))


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return None

class InstantiateCSVError(Exception):

        def __init__(self):
            self.message = "Файл item.csv поврежден"

        def __str__(self):
            return self.message