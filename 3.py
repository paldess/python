
while True:

    month = input('Введите месяц: \n')
    if month.isdigit() and range(1, 13):
        month = int(month)
        kalendar = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
        kalendar_dict = dict(Зима=[12, 1, 2], Весна=[3, 4, 5], Лето=[6, 7, 8], Осень=[9, 10, 11])
        if month in range(1, 13):
            #----------------- Решение через список --------------------
            print(f'Месяц № {month} это {kalendar[month-1]}')
            # ----------------- Решение через словарь --------------------
            for i in kalendar_dict:
                if month in kalendar_dict[i]:
                    print(f'Месяц № {month} это {i}')
                    break

    else:
        print('Введите корректные данные')
