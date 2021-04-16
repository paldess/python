def delen(x, y):
    while y == 0:
        print('На 0 делить нельзя!!!')
        x = int(input('Попробуйте ввсти еще раз: \nпервое число: '))
        y = int(input('второе число: '))
    return x/y



print(delen(int(input('Введите первое число: ')), int(input('Ввдите второе число:  '))))