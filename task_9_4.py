from random import choice


class Car:
    speed = 30, 40, 50, 60, 70
    color = 'black', 'white', 'yellow', 'grey'
    name = 'Mazda', 'Ferrari', 'Ford', 'Chevrolet'
    is_police = True, False
    direction = 'повернула налево', 'повернула направо', 'едет прямо', 'развернулась'

    def go(self):
        self.name = choice(Car.name)
        self.color = choice(Car.color)
        return f'Машина марки {self.name}, цвета {self.color} поехала'

    def stop(self):
        return f'Машина марки {self.name}, цвета {self.color} остановилась'

    def turn(self):
        self.direction = choice(Car.direction)
        return f'Машина {self.direction}'

    def show_speed(self):
        self.speed = choice(Car.speed)
        return f'Текущая скорость {self.speed}'


class TownCar(Car):
    is_police = Car.is_police[1]

    def show_speed(self):
        self.speed = choice(Car.speed)
        if self.speed > 60:
            return f'Превышение скорости на {self.speed - 60}'
        return f'Текущая скорость {self.speed}'


class SportCar(Car):
    is_police = Car.is_police[1]


class WorkCar(Car):
    is_police = Car.is_police[1]

    def show_speed(self):
        self.speed = choice(Car.speed)
        if self.speed > 40:
            return f'Превышение скорости на {self.speed - 40}'
        return f'Текущая скорость {self.speed}'


class PoliceCar(Car):
    is_police = Car.is_police[0]


t = TownCar()
print(f'{t.go()} --> {t.turn()} --> {t.show_speed()} --> {t.stop()}')
s = SportCar()
print(f'{s.go()} --> {s.turn()} --> {s.show_speed()} --> полиция: {s.is_police}')
w = WorkCar()
print(f'{w.go()} --> {w.turn()} --> {w.show_speed()} --> {w.turn()} --> {w.stop()}')
p = PoliceCar()
print(f'{p.go()} --> {p.show_speed()} --> полиция: {p.is_police}')
