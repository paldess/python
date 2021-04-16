def my_func(x, y):
    out = x
    for _ in range(1, y):
        out *= x
    return out
while True:
    try:
        number = float(input('Введите действительное число: '))
        stepen = int(input('В какую степень возвести?  '))
        break
    except ValueError:
        print('-' * 25)
        print('Введите корректные данные!')
        print('-' * 25)


print(my_func(number, stepen))