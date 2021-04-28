class Stationery:
    def __init__(self):
        self.title = 'отрисовка'

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        self.title = 'отрисовка ручкой'
        return self.title

class Pencil(Stationery):
    def draw(self):
        self.title = 'отрисовка карандашом'
        return self.title

class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__()
    def draw(self):
        self.title1 = 'отрисовка маркером'
        return self.title, self.title1

a = Stationery()
a.draw()
b = Pen()
print(b.draw())
c = Handle()
print(c.draw())

