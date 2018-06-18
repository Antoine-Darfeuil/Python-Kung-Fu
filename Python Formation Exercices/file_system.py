from abc import *


class Element(metaclass=ABCMeta):

    def __init__(self, name):
        self._checkName(name)
        self._name = name

    @abstractproperty
    def size(self):
        pass

    @abstractproperty
    def absoluteName(self):
        pass

    def _checkName(self, name):
        if name == '': raise ValueError("Incorrect name.")

    def __del__(self):
        print("Remove {}".format(self._name))


class Folder(Element):

    # Classe embarqée:
    class File(Element):

        def __init__(self, name, size):
            super().__init__(name)
            self._size = size

        @property
        def size(self):
            return self._size

        def __del__(self):
            super().__del__()
   
    _root = None

    @classmethod
    def root(cls):
        if cls._root == None:
            cls._root = cls("/")
        return cls._root
    
    def __init__(self, name):
        super().__init__(name)
        self._name = name
        self.elements = set()

    def createFile(self, fileName, fileSize):
        self.elements.add(Folder.File(fileName, fileSize))

    def createFolder(self, folderName):
        folder = Folder(folderName)
        self.elements.add(folder)
        return folder
       

    @property
    def size(self):
        self._size = 0
        for elt in self.elements:
            self._size += elt.size
        return self._size


    def __str__(self):
        out = ''
        for elt in self.elements:
            out += elt._name + '\n'
        return out

    def __repr__(self):
        return self.__str__()

    def __del__(self):
        for elt in self.elements:
            elt.__del__()
        #self.elements = set()
        super().__del__()


if __name__ == '__main__':

    #################
    # Customer test #
    #################
    # f2 = File("R1/R2/F2", 362)
    # R2.size
    # f1 = File("R1/F1", 1234)


    r1 = Folder.root()                                  #
    r1.createFile(fileName="F1", fileSize=1234)         #
    r2 = r1.createFolder(folderName="R2")               #
    r2.createFile("F2", 999)                            #
    print(r1.size)
    print(r1)
    print(r2.absoluteName)
