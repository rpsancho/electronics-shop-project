from src.item import Item


class Phone(Item):
    __number_of_sim = 0

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        # if number_of_sim > 0 and isinstance(number_of_sim, int):
        #     self.__number_of_sim = number_of_sim
        # else:
        #     raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        if num > 0 and isinstance(num, int):
            self.__number_of_sim = num
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"
