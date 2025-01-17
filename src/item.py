import csv

class InstantiateCSVError(BaseException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else '_Файл item.csv поврежден_.'

    def __str__(self):
        return self.message


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
        if not name or not price or not quantity:
            print('_Файл item.csv поврежден_')
        self.name = name
        self.price = price
        self.quantity = quantity
        super().__init__()
        #self.all.append(self)
    def __str__(self):
        return self.name
    def __repr__(self):
        return f'Item(\'{self.name}\', {self.price}, {self.quantity})'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return int(self.quantity) + int(other.quantity)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name)>=10:
            raise ValueError('Длина наименования товара превышает 10 символов.')
        self.__name = new_name


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
        try:
            with open('C:\Dev\electronics-shop-project\src\items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    item = cls(row['name'], row['price'], row['quantity'])
                    return item
        except FileNotFoundError:
            return '_Отсутствует файл item.csv_'
    # @staticmethod
    # def string_to_number(num):
    #     print (int(num))
