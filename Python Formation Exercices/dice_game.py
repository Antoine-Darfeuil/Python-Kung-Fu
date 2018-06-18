import random

class Dice:
    def __init__(self):
        self.throw()

    def throw(self):
        self.value = random.randint(1, 6)
    

class Cup:
    def __init__(self, nb_dices):
        self._checkEntries(nb_dices)
        self.dices = tuple(Dice() for _ in range(nb_dices))
        self.score = 0

    def __str__(self):
        return str([d.value for d in self.dices])
         
    def roll(self):
        self.score = 0
        for d in self.dices:
            d.throw()
            self.score += d.value
        s = set([d.value for d in self.dices])
        if len(s) == 1:
            self.score *= 2

    def _checkEntries(self, nb_dices):
        if type(nb_dices) is not int:
            raise TypeError("Number of dices should be an interger.")
        elif nb_dices <= 0:
            raise ValueError("Number of dice should be greater than 0.")


class LazyCup:
    """ Lazy Computing Design Pattern"""
    def __init__(self, nb_dices):
        self._checkEntries(nb_dices)
        self.dices = tuple(Dice() for _ in range(nb_dices))
        self._invalidValue()

    def __str__(self):
        return str([d.value for d in self.dices])
         
    def roll(self):
        for d in self.dices:
            d.throw()
        self._invalidValue()

    def __repr__(self):
        if self._valueIsInvalid():
            self._value = 0
            for dice in self.dices:
                self._value += dice.value         
        s = set([d.value for d in self.dices])
        if len(s) == 1:
            self._value *= 2
        return str(self._value)

    def _checkEntries(self, nb_dices):
        if type(nb_dices) is not int:
            raise TypeError("Number of dices should be an interger.")
        elif nb_dices <= 0:
            raise ValueError("Number of dice should be greater than 0.")

    def _invalidValue(self):
        self._value = None
        
    def _valueIsInvalid(self):
        self._value == None

      
class Game:
    def __init__(self):      
        pass

    def setup(self, nb_turns, nb_dices):
        self._checkEntries(nb_turns, nb_dices)
        self.players = []
        self.nb_turns = nb_turns
        self.cup = Cup(nb_dices)

    def enroll(self, *player_names):
        for name in player_names:
            self.players.append(Player(name))        
                            
    def start(self):
        for turn in range(self.nb_turns):
            self._playTurn(turn)
        self._displayWinner()

    def _playTurn(self, turn):
        print("Turn {}".format(turn+1))
        for player in self.players:
            player.play(self.cup)
    
    def _displayWinner(self):
        winner = max(self.players)
        print("{} win with {}".format(winner.name, winner.score))

    def _checkEntries(self, nb_turns, nb_dices):
        if type(nb_turns) is not int:
            raise TypeError("Number of turns should be an interger.")
        elif nb_turns <= 0:
            raise ValueError("Number of turns should be greater than 0.")
                
               
class Player:
    def __init__(self, name):
        self._checkEntries(name)
        self.name = name
        self.score = 0

    def play(self, cup):
        cup.roll()
        self.score += cup.score
        print("{} got {} --> score: {}".format(self.name, cup, self.score))

    def __eq__(self, other):
        return self.score == other.score
    
    def __lt__(self, other):
        self._checkObj(other)
        if self == other:
            return self.name > other.name
        else:
            return self.score < other.score

    def _checkObj(self, obj):
        if type(obj) != type(self):
            raise TypeError("Can compare object of type {} with object of type {}.".format(type(obj), type(self)))

    def _checkEntries(self, name):
        if type(name) is not str:
            raise TypeError("Player name should be a string.")
        elif name == '':
            raise NameError("You must define a player name.")
        

# =========================================================================================== #
# =========================================================================================== #

def test1():
    d1 = Dice()
    print(d1.value)
    d1.throw()
    print(d1.value)
    del d1

def test2():
    cup = Cup(2)
    cup.roll()
    cup.roll()
    del cup

def main():
    game = Game()
    game.setup(20, 2)
    game.enroll("Bob", "Alice", "Charles")
    game.start()    


if __name__ == '__main__':

    test1()
    test2()
    main()




