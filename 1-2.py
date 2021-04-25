from os import listdir, remove
while True:
    print('*'*30)
    deistv = input('Выберите: \n'
                   '1-создание файла\n'
                   '2-удаление\n'
                   '3-дописать в файл\n'
                   '4-вывести кол-во строк и слов\n'
                   'q-выход\n')
    print('*' * 30)
    if deistv == 'q':                                                   # выход
        exit()
    elif deistv == '1':                                                 # создание
        name = input('Введите название файла: ')
        with open(f'{name}.txt', 'w') as txt:
            pass
        write_ = input(f'Файл {name}.txt успешно создан. \nЗаписать в файл информацию?\n1-да, 2-нет:')
        if write_ == '2':
            continue
        elif write_ == '1':
            text_ = input('Что запишем в файл?: \n')
            with open(f'{name}.txt', 'a') as txt:
                txt.write(text_ + '\n')
        else:
            print('Некорректный ввод')
    elif deistv == '2':                                                                # удаление
        print('*'*30)
        for i in listdir(path='.'):
            print(i)
        print('*'*30)
        name_del = input('Какой файл вы хотите удалить?(без расширения txt): \n'
                         '*для отмены - q\n')
        if name_del == 'q':
            continue
        remove(f'{name_del}.txt')
        print(f'Файл {name_del}.txt удален')
    elif deistv == '3':                                                              # дозапись
        name = input('В какой файл запишем?(без расширения txt): \n')
        text_ = input('Что запишем в файл?: \n')
        if text_ == None:
            print('Досвидания!')
            exit()
        with open(f'{name}.txt', 'a') as txt:
            txt.write(text_ + '\n')
    elif deistv == '4':
        for i in listdir(path='.'):
            print(i)
        file = input('Выберите файл(без разрешения .тхт):  ')
        with open(f'{file}.txt', 'r') as txt:
            txt = txt.read()
        txt = txt.split('\n')
        print(f'В файле {file}.txt - {len(txt)} строк')
        for i , j in enumerate(txt, 1):
            j = j.split()
            print(f'В {i} строке - {len(j)} слов\n')
    else:
        print('Некорректный выбор')
