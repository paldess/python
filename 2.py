from abc import abstractmethod

class Garment:
    def __init__(self):
        self.vid = 'это одежда'
        self.cloth = 1


    def __add__(self, other):
        x = self.cloth + other.cloth
        return x



    @property
    def list(self):
        return f'{self.vid} и на это уходит {self.cloth} ткани'
    @abstractmethod
    def __str__(self):
        return self.vid


class Palto(Garment):
    def __init__(self, v):
        Garment.__init__(self)
        self.vid = 'это пальто'
        self.cloth = round(v / 6.5 + 0.5, 3)


class Costume(Garment):
    def __init__(self, h):
        super().__init__()
        self.vid = 'это костюм'
        self.cloth = round(2 * (h / 100) + 0.3, 3)


dress = Garment()
print(dress)
dress1 = Palto(5)
print(dress1)
print(dress1.cloth)
dress3 = Costume(172)
print(dress3)
print(dress3.cloth)
print(dress3.list)
a = dress3 + dress1
print(a)
print(dress3 + dress1)
