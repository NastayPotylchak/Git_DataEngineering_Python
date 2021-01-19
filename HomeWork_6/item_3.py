# Класс Работник
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position)
        self._income = _income

    def get_full_name(self):
        return (f"{self.surname} {self.name} ")

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

dict_position_1 = {"wage": 10000, "bonus": 5300}
position_1 = Position("Kate", "Tarasova", "Manager", dict_position_1)
print('******************position_1******************')
print(position_1.get_full_name())
print(f"Доход = {position_1.get_total_income()}")

dict_position_2 = {"wage": 25600, "bonus": 7900}
position_2 = Position("Ivan", "Petrov", "Programmer", dict_position_2)
print('******************position_2******************')
print(position_2.get_full_name())
print(position_2.get_total_income())

dict_position_3 = {"wage": 17900, "bonus": 4100}
position_3 = Position("Fedor", "Vodkin", "Specialist", dict_position_3)
print('******************position_3******************')
print(position_3.get_full_name())
print(position_3.get_total_income())
