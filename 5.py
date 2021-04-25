number = input('Введите числа через пробел: \n')
number = number.split()
summ = 0
with open('zadanie-5.txt', 'w') as tt1:
    pass
with open('zadanie-5.txt', 'a') as tt:
    for i in number:
        if i.replace('-', '.').replace('.', '').isdigit():
            tt.write(i + '\n')
            summ += float(i)
        else:
            print('Введена не цифра. Пропускаю')
            continue
with open('zadanie-5.txt', 'a') as tt:
    tt. write(f'Сумма чисел равна: {summ}')
print('*'*25 + '\n')
print(f'Сумма чисел равна: {summ}')