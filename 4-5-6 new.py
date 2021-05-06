class Sklad():                                                              # класс склад
    def __init__(self):
        self.sklad = []

    def __str__(self):                                                      # вывод заполненности склада
        print('На складе:  ')
        print('*' * 40)
        for i in self.sklad:
            print(i.__dict__)
        return ('*' * 40)

    def add_to_sklad(self, obj):                                                # добавление на склад
        self.sklad.append(obj)

    def del_sklad(self, obj, type_orgtehnics, volume):                          # удаление со склада
        for i in self.sklad:
            if i.name == obj and i.type_orgtehnics == type_orgtehnics:          # нахождение удаляемого обьекта
                if i.volume > volume:
                    i.volume = str(int(i.volume) - int(volume))
                elif i.volume == volume:
                    self.sklad.remove(i)
                else:
                    print('на складе недостаточно техники')
                return ''
        print('*' * 40)
        print('данных товаров не найдено')
        print('*' * 40)
class Orgtehnica():                                     #класс оргтехника
    def __init__(self):
        self.type_orgtehnics = 'unknown'
        self.type_primeneniya = 'home'
        while True:
            x = input('Введите количество: ')
            if x.isdigit():
                if int(x) > 0:
                    self.volume = x
                    break
            print('*' * 40)
            print('Введите только целые положительные числа больше 0!!!')
            print('*' * 40)




class Printer(Orgtehnica):                      #создание класса принтер
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type_orgtehnics = 'printer'
        self.type = 'lazer'

class Scaner(Orgtehnica):                       #создание класса сканер
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type_orgtehnics = 'scaner'
        self.type = 'color'

class Kserox(Orgtehnica):                       # создание класса ксерокс
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type_orgtehnics = 'kserox'
        self.type = 'МФУ'

sklad = Sklad()                                     # инициализация первого и единственного обьекта "склад"

while True:                                         # постоянный цикл для повторения циклов

    deistv = input('Выберите действие:\n1-добавить на склад\n2-удалить со склада\n3-показать содержимое склада\n4-выход\n')         # выбор действия
    if deistv == '4':                                                                                                               # выход
        exit()

    elif deistv == '1':                                                                                                             # добавить на склад
        what = input('Что завозим на склад?:\n1-принтеры\n2-сканеры\n3-ксероксы\n4-отменить\n')
        if what == '4':
            continue
        elif what == '1':
            name = input('Введите название принтера: ')
            a = Printer(name)
            sklad.add_to_sklad(a)
        elif what == '2':
            name = input('Введите название сканера: ')
            a = Scaner(name)
            sklad.add_to_sklad(a)
        elif what == '3':
            name = input('Введите название ксерокса: ')
            a = Kserox(name)
            sklad.add_to_sklad(a)

    elif deistv == '2':                                                                                                     # удаление со склада
        what = input('Что увозим со склада?:\n1-принтеры\n2-сканеры\n3-ксероксы\n4-отменить\n')
        if what == '4':
            continue
        elif what == '1':
            name = input('Введите название принтера: ')
            while True:
                x = input('Сколько принтеров увозим? ')
                if x.isdigit():
                    if int(x) > 0:
                        volume = x
                        break
                print('*' * 40)
                print('Введите только целые положительные числа больше 0!!!')
                print('*' * 40)
            sklad.del_sklad(name, 'printer', volume)
        elif what == '2':
            name = input('Введите название сканера: ')
            while True:
                x = input('Сколько сканеров увозим? ')
                if x.isdigit():
                    if int(x) > 0:
                        volume = x
                        break
                print('*' * 40)
                print('Введите только целые положительные числа больше 0!!!')
                print('*' * 40)
            sklad.del_sklad(name, 'scaner', volume)
        elif what == '3':
            name = input('Введите название ксерокса: ')
            while True:
                x = input('Сколько ксероксов увозим? ')
                if x.isdigit():
                    if int(x) > 0:
                        volume = x
                        break
                print('*' * 40)
                print('Введите только целые положительные числа больше 0!!!')
                print('*' * 40)
            sklad.del_sklad(name, 'kserox', volume)

    elif deistv == '3':                                                                                                         # вывод содержимого склада
        print(sklad)

