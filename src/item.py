# import pathlib
import csv
#from pathlib import Path
#path = Path("Dev", "electronics-shop-project", "src", "items.csv")


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self):
        assert len(self.__name) >= 11, 'Длина наименования товара превышает 10 символов.'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:\Dev\electronics-shop-project\src\items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = (row['name'], row['price'], row['quantity'])
                return (cls(item))

    @staticmethod
    def string_to_number(num):
        num_int = int(num)
        return num_int
