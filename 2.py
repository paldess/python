class MyError(Exception):
    def __init__(self):
        print('кажется ошибочка - делим на 0')
class MyErrorSimbol(Exception):
    def __init__(self):
        print('кажется ошибочка - знаки')

try:
    number1 = input('Введите первое число:  ')
    number2 = input('Введите второе число:  ')
    number11 = number1.replace('.', '')
    number22 = number2.replace('.', '')
    if not number11.isdigit():
        raise MyErrorSimbol
    elif not number22.isdigit():
        raise MyErrorSimbol

    if float(number2) == 0:
        raise MyError
    print(float(number1) / float(number2))
except MyErrorSimbol:
    print('введены не цифры')

except MyError:
    print('На 0 делить нельзя... пока что)')