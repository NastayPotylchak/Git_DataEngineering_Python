# Класс Дорога

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width  = _width

    def calc_weight(self, weight, thickness):
        return self._length * self._width * weight / 1000 * thickness

road = Road(20, 5000)
weight = road.calc_weight(25, 5)
print(f"Масса асфальта = {weight} т.")