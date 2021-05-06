class MyClass(Exception):
    def __init__(self, typ):
        print('-' * 30)
        print(f'"{typ}" <-это не число. Вводите только числа')
        print('-' * 30)

list = []
while True:
    number = input('***Введите число либо "q" для выхода:***   ')
    try:
        if number == 'q':
            exit()
        number1 = number.replace('.', '').replace('-', '')
        if not number1.isdigit():
            raise MyClass(number)

        list.append(float(number))
        print('*' * 30)
        print(list)
        print('*' * 30)
    except MyClass:
        print(list)
