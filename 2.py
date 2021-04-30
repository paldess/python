from abc import abstractmethod, ABC


class Garment:

    def __init__(self):
        self.vid = 'это одежда'
        self.cloth = 0

    @abstractmethod
    def __str__(self):
        return self.vid


class Palto(Garment, ABC):
    def __init__(self, v):
        super().__init__()
        self.vid = 'это пальто'
        self.cloth = round(v / 6.5 + 0.5, 3)


class Costume(Garment, ABC):
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
