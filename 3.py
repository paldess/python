
class Worker:
    def __init__(self, name, surname, position, *zp):
        self.name = name
        self.surname = surname
        self.position = position
        self.__incom = {'wage': zp[0], 'bonus': zp[1]}

    def get_total(self):
        wage = self.__incom['wage']
        bonus = self.__incom['bonus']
        return  wage, bonus
class Position(Worker):
    def get_full_name(self):
        print(f'Имя: {self.name} \nФамилия: {self.surname}')
    def get_total_income(self):
        x, y = Worker.get_total(self)
        print(f'Зп с учетом бонуса: {int(x) / 100 * int(y) + int(x)}')

a = Worker('Василий', 'Тапочкин', 'раб', '5000', '50')
Position.get_full_name(a)
Position.get_total_income(a)