import random
from abc import *


class Rollable(metaclass=ABCMeta):
    @abstractmethod
    def roll(self):
        pass

    @abstractmethod
    def getValue(self):
        pass


class Dice(Rollable):

    def __init__(self):
        self.roll()

    def roll(self):
        self.value = random.randint(1, 6)

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.value)


class Coin(Rollable):

    def __init__(self):
        self.roll()

    def roll(self):
        self.side = random.randint(0, 1)

    def getValue(self):
        if self.side == 0:
            return 3
        else:
            return 0

    def __str__(self):
        if self.side == 0:
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
        self.getValue()

    def roll(self):
        for rollable in self.rollables:
            rollable.roll()

    def getValue(self):
        self.values = [rollable.getValue() for rollable in self.rollables]
        self.value = sum(self.values)
        if set(self.values) == 1: self.value *= 2
        return self.value

    def __str__(self):
        return "Cup:" + str(self.values)



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
        print(c, ":", c.getValue())

    print("CUP:")
    c = Cup(Dice, 4)
    print(c)

    for _ in range(20):
        c.roll()
        print(c, ":", c.getValue())
