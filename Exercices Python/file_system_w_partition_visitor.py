from abc import *
import time


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

    def display(self, tab=""):
        # Pattern Template Method
        out = "{}{}: {}".format(tab, self.type, self._name) # etape obligatoire
        print(out)
        self._onDisplayed(tab) # etape facultative

    @abstractproperty
    def type(self):
        pass

    def _onDisplayed(self, tab):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass



class Folder(Element):
    _tabs = 0

    # Classe embarqée:
    class File(Element):

        def __init__(self, name, parent, size):
            if Partition.instance()._checkSize(size):
                super().__init__(name, parent)
                self._size = size
            else:
                raise ValueError("ARRRRRRGGG!!")

        @property
        def size(self):
            return self._size

        def __str__(self):
            return self._name
        
        def __repr__(self):
            return self.__str__()

        def __del__(self):
            super().__del__()

        @property
        def type(self):
            return "file"

        def accept(self, visitor):
            visitor.visitFile(self)
   
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

    def __iter__(self):
        return iter(self.elements)

    @property
    def type(self):
        return "folder"
    
    def _onDisplayed(self, tab):
        ntab = tab + "    "
        for elt in self.elements:
            time.sleep(0.2)
            elt.display(ntab)   

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

    def __str__(self):
        return self._name

    def __repr__(self):
        return self.__str__()

    def __del__(self):
        for elt in self.elements:
            elt.__del__()
        #self.elements = set()
        super().__del__()


    def accept(self, visitor):
        #Visitor Design pattern
        visitor.visitFolder(self)
        for elt in self.elements:
            elt.accept(visitor)


class Partition(Folder):
    _instance = None

    def __init__(self, name, capacity):
        super().__init__(name, None)
        self._capacity = capacity


    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls("sba", capacity=1000) # lecture d'un fichier de config
        return cls._instance
        

    def _checkSize(self, file_size):
        if (self._capacity - self.size) >= file_size:
            print("Free space: {}".format(self._capacity - self.size))
            return True
        return False

    @property
    def type(self):
        return "partition"








class Visitor(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def visitFolder(self, folder):
        pass

    @abstractmethod
    def visitFile(self, file):
        pass


class CountTool:

    def __init__(self):
        self.__nbFolders = 0
        self.__nbFiles = 0
        
    def visitFolder(self, folder):
        self.__nbFolders += 1

    def visitFile(self, file):
        self.__nbFiles += 1
        
        
    def __str__(self):
        return "{} folders ; {} files".format(self.__nbFolders, self.__nbFiles)
        

class SizeTool:

    def __init__(self):
        self.__size = 0
        
    def visitFolder(self, folder):
        pass

    def visitFile(self, file):
        self.__size += file.size
                
    def __str__(self):
        return "folder size: {} bits".format(self.__size)


    

if __name__ == '__main__':

    sba = Partition.instance()

    sba.createFile(fileName="F1", fileSize=124)          #
    r1 = sba.createFolder(folderName="Document")                #
    r2 = r1.createFolder(folderName="Travail")                 #
    r3 = r1.createFolder(folderName="Personnel")                 #
    r4 = r2.createFolder(folderName="Mechanical Design")                 #
    r5 = r4.createFolder(folderName="Robot1")                 #
    r6 = r5.createFolder(folderName="Parts")                 #
    sba.createFile("Document1", 12)
    sba.createFile("Document2", 13)   
    r2.createFile("Report1", 99)                              #
    r3.createFile("Letter1", 12)                               #
    print(r1.size)
    print(r1)
    print(r4.absoluteName)

    print("\n"*2)
    sba.display()

    tool = CountTool()
    sba.accept(tool)
    print(tool)

    tool = SizeTool()
    sba.accept(tool)
    print(tool)
