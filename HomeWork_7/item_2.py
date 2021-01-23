#Класс Одежда
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, description):
        self.description = description

    @abstractmethod
    def expense_material(self):
        pass

class Coat(Clothes):
    def __init__(self, description, size):
        super().__init__(description)
        self.size = size
    @property
    def expense_material(self):
        return (round(self.size/6.5 + 0.5, 2))

class Suit(Clothes):
    def __init__(self, description, height):
        super().__init__(description)
        self.height = height

    @property
    def expense_material(self):
        return (round(2 * self.height + 0.3))

coat = Coat("Мужское пальто", 52)
print('Расход ткани на пальто = ', coat.expense_material)

suit = Suit('Женский костюм', 160)
print('Расход ткани костюма = ', suit.expense_material)

