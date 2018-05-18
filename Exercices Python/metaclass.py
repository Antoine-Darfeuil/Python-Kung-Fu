from abc import *

class Shape(metaclass=ABCMeta):
    '''
    Pas instanciable ; mais pas forcement vide.
    Definie un contract à respecter.
    '''

    @abstractmethod
    def getArea(self):
        '''Oblige les sous-classes à posséder cette méthode -> sinon fails !'''
        pass


class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.h = height
        self.w = width

    def getArea(self):
        return self.h * self.w


class Circle(Shape):

    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return 3.14 * self.radius**2



if __name__ == '__main__':

    c = Circle(r=12)
    r = Rectangle(45, 10)
    print(c.getArea())
    print(r.getArea())

    try:
        s = Shape()
    except:
        print("Can't do that, Sorry")
