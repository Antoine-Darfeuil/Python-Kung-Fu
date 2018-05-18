from abc import *


class Element(metaclass=ABCMeta):

    def __init__(self, name, parent):
        self._checkName(name)
        self._name = name
        self._parent = parent

    @abstractproperty
    def size(self):
        pass

    @property
    def absoluteName(self):
        absName = ""
        if self._parent is not None and self._parent._parent is not None:
            absName += self._parent.absoluteName + "/"
        else:
            absName = "/"
        return absName + self._name

    def _checkName(self, name):
        if name == '': raise ValueError("Incorrect name.")

    def __del__(self):
        print("Remove {}".format(self._name))


class Folder(Element):

    # Classe embarqée:
    class File(Element):

        def __init__(self, name, parent, size):
            super().__init__(name, parent)
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
            cls._root = cls("/", None)
        return cls._root
    
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self._name = name
        self.elements = set()
        self._size = None

    def createFile(self, fileName, fileSize):
        self.elements.add(Folder.File(fileName, self, fileSize))
        if fileSize != 0:
            self._invalidSize()

    def createFolder(self, folderName):
        folder = Folder(folderName, self)
        self.elements.add(folder)
        return folder
       

    @property
    def size(self):
        if self._sizeIsInvalid():
            print("Computing size ...")
            self._size = 0
            for elt in self.elements:
                self._size += elt.size
        return self._size

    def _invalidSize(self):
        if self._parent: self._parent._invalidSize()
        print("Invalidate size for {}".format(self._name))
        self._size = None

    def _sizeIsInvalid(self):
        return self._size == None

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


    root = Folder.root()                                  #
    root.createFile(fileName="F1", fileSize=1234)         #
    r1 = root.createFolder(folderName="R1")               #
    r2 = r1.createFolder(folderName="R2")                 #
    r3 = r1.createFolder(folderName="R3")                 #
    r4 = r2.createFolder(folderName="R4")                 #
    r5 = r4.createFolder(folderName="R5")                 #
    r6 = r5.createFolder(folderName="R6")                 #
    r2.createFile("F2", 999)                              #
    r3.createFile("F3", 12)                              #
    print(r1.size)
    print(r1)
    print(r4.absoluteName)
