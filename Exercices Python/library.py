class Document():
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def __str__(self):
        return self.title
        


class Book(Document):
    _compter = 0
    
    def __init__(self, isbn, title, author, genre):
        super().__init__(isbn, title)
        self.author = author
        self.genre = genre
        Book._compter += 1

    def __del__(self):
        Book._compter -= 1


    def __str__(self):
        return "BOOK: {} [{}]".format(super().__str__(), self.author)


class Video(Document):

    def __init__(self, code, title, real, length):
        super().__init__(code, title)
        self.real = real
        self.length = length

    def __str__(self):
        return "VIDEO: {} [{}]".format(super().__str__(), self.real)
        
        

class Library():

    def __init__(self):
        self.books = {}
        self._videos = {}
        self.docs = {'books': self.books , 'videos': self._videos}

    def addBook(self, *, isbn, title, author, genre):
        if isbn not in self.books:
            self.books[isbn] = set()
        self.books[isbn].add(Book(isbn, title, author, genre))

    def addVideo(self, *, code, title, real, length):
        if code not in self._videos:
            self._videos[code] = set()
        self._videos[code].add(Video(code, title, real, length))


    """
    def displayAll(self):
        '''Display function => Bad design.'''
        for isbn, books in self.collection.items():
            for book in books:
                print("{} : \t {}".format(isbn, book))
    """

    def __str__(self):
        out = '-'*50 + '\n'
        for media, collection in self.docs.items():
            for code, set_obj in collection.items():
                for obj in set_obj:
                    out += "{} : \t {}\n".format(code, obj)
        return out

    def _getvideos(self):
        for item in self:
            if isinstance(item, Video):
                yield item
                
    def videos(self):
        return self._getvideos()
        
    def __iter__(self):
        for media, collection in self.docs.items():
            for code, set_item in collection.items():
                for item in set_item:
                    yield item

        

def main():
    lib = Library()
    lib.addBook(isbn="ZO45", title="Germinal", author="Zola", genre="Novel")
    lib.addBook(isbn="ZO45", title="Germinal", author="Zola", genre="Novel")
    lib.addBook(isbn="PY67", title="Python for Dummies", author="Jean-Mi", genre="Education")
    lib.addBook(isbn="CON57", title="1984", author="George Orwell", genre="Novel")
    lib.addVideo(code="HAL50", title="2001", real="Kubick", length="120")

    for vid in lib.videos():
        print(vid)
    
    print('-'*50)
    for item in lib:
        print(item)

    print(lib)
    return lib

if __name__ == '__main__':
    lib = main()
