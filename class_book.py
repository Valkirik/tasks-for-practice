class Library:
    LIBRARY = {}
    def __init__(self, name: str, author: str, year: int, available = True):
        self.name = name
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return f"{self.name}: {self.author}"

    @classmethod
    def get_library(cls):
        return Library.LIBRARY

    def add_book(self):
        book = {"author": self.author, "year": self.year, "available": self.available}
        if self.name in Library.LIBRARY:
            print(f"The book '{self.name}' is already in the library")
        else:
            Library.LIBRARY[self.name] = book


    def remove_book(self):
        if self.name in Library.LIBRARY:
            del Library.LIBRARY[self.name]
        else:
            print(f"The book '{self.name}' is not in the library")

    def borrow_book(self):
        s = Library.LIBRARY[self.name]
        if s['available'] is True:
            s['available'] = False
            self.available = False

        else:
            print(f"The book '{self.name}' is already borrowed")


book_1 = Library("Война и мир", "Лев Толстой", 1900)
book_2 = Library("Унесенные ветром", "Маргарет Митчел", 1960)
book_3 = Library("Уловка 22", "Джлзеф Хеллер", 1960)


book_1.add_book()
book_2.add_book()

print(Library.LIBRARY)
book_2.borrow_book()
print(Library.LIBRARY)

book_2.borrow_book()



















