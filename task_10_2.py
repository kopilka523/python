from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def coat_method(self):
        pass

    @abstractmethod
    def suit_method(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat_method(self):
        return round(self.v / 6.5 + 0.5)

    @property
    def suit_method(self):
        return round(2 * self.h + 0.3)


mc = Clothes(54, 182)
print(mc.suit_method + mc.coat_method)
