import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    CSV_PATH = '../src/items.csv'
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        try:
            f = open(cls.CSV_PATH, "r", encoding='windows-1251', newline='')
        except FileNotFoundError:
            # print('Отсутствует файл items.csv')
            raise FileNotFoundError("Отсутствует файл items.csv")

        init_data = csv.DictReader(f)
        for row in init_data:
            if not (row['name'] and row['price'] and row['quantity']):
                raise InstantiateCSVError
            else:
                cls(row['name'], float(row['price']), int(row['quantity']))
        f.close()

    @staticmethod
    def string_to_number(string):
        return int(float(string))

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
        self.price *= self.pay_rate


class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = "Файл items.csv поврежден"

    def __str__(self):
        return self.message
