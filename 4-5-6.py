
class Sklad():
    volume_sklad = 5
    list_sklada = []

    def __str__(self):
        for i in self.list_sklada:
            print(i.clas, i.name, end=', ')
        return ''

    def add_in_to_sklad(self, tehn):
        if len(self.list_sklada) >= self.volume_sklad:
            print('склад заполнен')
        else:
            self.list_sklada.append(tehn)
            print(f'{tehn.clas} {tehn.name} добавлена на склад')

    def dell_to_sklad(self, tehn):
        for i in range(len(self.list_sklada)):
            if self.list_sklada[i] == tehn:
                self.list_sklada.pop(i)
                print(f'{tehn} {tehn.name} удалено со склада')
                break

        print('данной техники на складе не найдено')

class Orgtehnica():
    def __init__(self):
        self.name = ''

    def __str__(self):
        return self.name


class Printer(Orgtehnica):
    def __init__(self, name):
        super().__init__()
        self.clas = 'printer'
        self.name = name

class Scaner(Orgtehnica):
    pass

class Kserox(Orgtehnica):
    pass





sklad = Sklad()

while True:
    dest = input('выберите действие-1-добавить, 2-удалить:   ')
    if dest == '1':
        r1= Printer(input())
        sklad.add_in_to_sklad(r1)
        print(sklad)
    elif dest =='2':
        r1 = Printer(input())
        sklad.dell_to_sklad(r1)
        print(sklad)
    # pr1 = Printer('mp-506')
    # pr2 = Printer('mp-108')
    # print(pr1.name)
    # sklad.add_in_to_sklad(pr1)
    # sklad.add_in_to_sklad(pr2)
    #
    # print(sklad)
    # sklad.dell_to_sklad(pr1)
    # print(sklad)