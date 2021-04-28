
class Road:
    def __init__(self, length, width):
        self.__length = int(length)
        self.__width = int(width)

    def massa(self):
        return (self.__length * self.__width * 25 * 5 / 1000)

result = Road(input('Введите длину асфальта в метрах:  '), input('Введите ширину асфальта в метрах:  '))
print(f'{result.massa()} т.')