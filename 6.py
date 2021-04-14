osnov = {'Название': 0, 'Цена': 0, 'Количество': 0, 'Единица измерения': 0}
schet = 0
struktura = []
while True:
    act = input('Выберите действие: 1-добавить товар, 2-просмотреть товары, 3-посмотреть количество товаров в базе, '
            '\n4-названия товаров, 5-общую стоимость, 6-общее количество, 7-собрать аналитику, exit - для завершения сеанса: \n')
    if act == '1':
        schet += 1
        tovar = []
        tovar.append(schet)
        osnov['Название'] = input('Введите название товара:  ')
        q= input('Введите цену товара:  ')
        while q.replace('.', '').isdigit() == False:
            print('Введите корректную цену')
            q = input('Введите цену товара:  ')
        osnov['Цена'] = q
        q = input('Введите кол-во товара:  ')
        while q.replace('.', '').isdigit() == False:
            print('Введите корректное кол-во')
            q = input('Введите кол-во товара:  ')
        osnov['Количество'] = q
        osnov['Единица измерения'] = input('Введите единицы измерения товара:  ')

        tovar.append(osnov)
        tovar_tupl = tuple(tovar)
        print(tovar_tupl)
        struktura.append(tovar_tupl)

    elif act == '2':
        for i in struktura:
            print(i)
    elif act == '3':
        print(f'В базе числиться {schet} пунктов')
    elif act == '4':
        print('Наименования товаров:')
        for i in struktura:
            print(i[1]['Название'])
    elif act == '5':
        sum = 0
        for i in struktura:
            sum += int(i[1]['Цена'])
        print(sum)
    elif act == '6':
        sum = 0
        for i in struktura:
            sum += int(i[1]['Количество'])
        print(sum)
    elif act == '7':
        analitik = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
        for i in struktura:
            analitik['Название'].append(i[1]['Название'])
            analitik['Цена'].append(i[1]['Цена'])
            analitik['Количество'].append(i[1]['Количество'])
            analitik['Единица измерения'].append(i[1]['Единица измерения'])
        for i in analitik:
            print(i, '---', analitik[i])

    elif act == 'exit':
        break
    else:
        print('Введите корректный выбор')