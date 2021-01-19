# Класс Машина
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля = {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        over_speed = self.speed - 60
        message = f"Текущая скорость автомобиля = {self.speed}" if self.speed < 60 else \
            f"Превышение скорости на {over_speed}"
        print(message)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        over_speed = self.speed - 40
        message = f"Текущая скорость автомобиля = {self.speed}" if self.speed < 40 else\
            f"Превышение скорости {over_speed}"
        print(message)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

print('------------------TownCar------------------')

town_car = TownCar(40, 'white', 'Volga', False)
print(town_car.color, town_car.name)
town_car.go()
town_car.turn('право')
town_car.show_speed()
town_car.speed = 90
town_car.show_speed()
town_car.stop()

print('------------------SportCar------------------')

sport_car = SportCar(90, 'red', 'Ferrari', False)
print(sport_car.color, sport_car.name)
sport_car.go()
sport_car.show_speed()
sport_car.speed = 120
sport_car.show_speed()
sport_car.turn('лево')
sport_car.speed = 270
sport_car.show_speed()
sport_car.stop()

print('------------------WorkCar------------------')
work_car = WorkCar(30, 'grey', 'Gazel', False)
print(work_car.color, work_car.name)
work_car.go()
work_car.show_speed()
work_car.turn('лево')
work_car.turn('право')
work_car.speed = 55
work_car.show_speed()
work_car.stop()

print('------------------PoliceCar------------------')
police_car = PoliceCar(70, 'blue', 'Ford', True)
print(police_car.color, police_car.name, police_car.is_police)
police_car.go()
police_car.show_speed()
police_car.turn('право')
police_car.turn('лево')
police_car.speed = 90
police_car.show_speed()
police_car.stop()
