class Library:
    def __init__(self):
        self.books = []
        self.totalBooks = 0
    def addBooks(self, book):
        self.books.append(book)
        self.totalBooks += 1
    def info(self):
        print(f"Number of Books: {self.totalBooks}")
        
        for index,i in enumerate(self.books, start = 1):
            print(f"Book No {index}: {i}")
        
obj = Library()
obj.addBooks("Harry Potter")
obj.addBooks("Percy Jackson")
obj.addBooks("Goosbumps")
obj.info()