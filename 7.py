class Number():
    def __init__(self, number1, number2):
        self.number = complex(number1, number2)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number





a = Number(6, 1)
b = Number(2, -3)
print(a.number)
print(b.number)
print(a + b)
print(a * b)