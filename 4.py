class Car:
    def __init__(self, name, color, speed, is_police):
        self.name, self.color, self.speed, self.is_police = name, color, speed, bool(is_police)

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}!')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print('Превышение скорости')
class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print('Превышение скорости')

car_name = 'bmw'
car_color = 'black'
car_speed = 70
car_police_yn = 'y'
car_police = True if car_police_yn == 'y' else False
car1 = Car(car_name, car_color, car_speed, bool(car_police))

car_name = 'ваз'
car_color = 'grey'
car_speed = 30
car_police_yn = 'n'
car_police = True if car_police_yn == 'y' else False
car2 = Car(car_name, car_color, car_speed, bool(car_police))
# *********************************************************************************************
car1.go()
print('копы' if car1.is_police == True else 'свои')
car2.stop()
car2.turn('налево')
car1.turn('направо')

TownCar.show_speed(car1)
Car.show_speed(car1)
WorkCar.show_speed(car2)