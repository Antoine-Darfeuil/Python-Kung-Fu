import random
from abc import *



class Rollable(metaclass=ABCMeta):
    @abstractmethod
    def roll(self):
        pass

    @abstractproperty
    def value(self):
        pass


class Dice(Rollable):

    def __init__(self):
        self.roll()

    def roll(self):
        self._value = random.randint(1, 6)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)


class Coin(Rollable):

    def __init__(self):
        self.roll()

    def roll(self):
        self._side = random.randint(0, 1)

    @property
    def value(self):
        if self._side == 0:
            return 3
        else:
            return 0

    def __str__(self):
        if self._side == 0:
            return "Tails"
        return "Heads"
    

class Cup(Rollable):

    '''
    Design Pattern: 'Le Composite'.
    Est de type Rollable.
    Contient des Rollable.
    '''

    def __init__(self, rollableType, nb_rollable):
        if not issubclass(rollableType, Rollable): raise TypeError("rollableType must be a Rollable")
        self.rollables = set([rollableType() for _ in range(nb_rollable)])
        self._values = []

    def roll(self):
        for rollable in self.rollables:
            rollable.roll()

    @property
    def value(self):
        self._values = [rollable.value for rollable in self.rollables]
        self._value = sum(self._values)
        if set(self._values) == 1: self._value *= 2
        return self._value

    def __str__(self):
        return "Cup:" + str(self._values)



if __name__ == '__main__':

    d = Dice()
    print(d)
    for _ in range(20):
        d.roll()
        print(d)

    print("CUP:")
    c = Cup(Coin, 4)
    print(c)

    for _ in range(20):
        c.roll()
        print(c, ":", c.value)

    print("CUP:")
    c = Cup(Dice, 4)
    print(c)

    for _ in range(20):
        c.roll()
        print(c, ":", c.value)

 
