
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def make_order(self, n):
        if n <= 0:
            return 'невозможно.'
        result = str()
        for i in range(1, (self.quantity+1)):
            result += '*'
            if i % n == 0:
                result += '\n'
        return f'{result}'

    def __str__(self):
        return f'в классе {self.quantity} клеток '

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        # return self.quantity - other.quantity if self.quantity >= other.quantity else 'результат отрицателен'
        if self.quantity >= other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            return f'результат отрицателен: {self.quantity} - {other.quantity} = {self.quantity - other.quantity}'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity / other.quantity)


cell_1 = Cell(11)
cell_2 = Cell(3)
print(cell_2)
print(cell_2+cell_1)
print(cell_1-cell_2)
print(cell_2-cell_1)
print(cell_2*cell_1)
print(cell_2/cell_1)
print(Cell.make_order(cell_1, 2))