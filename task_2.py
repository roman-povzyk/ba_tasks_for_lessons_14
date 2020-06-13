class Library:
    def __init__(self, books, authors):
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        self.books.append(name, year, author)

class Book(Library):
    def __init__(self, name, year, author):
        super().__init__(name)
        self.year = year
        self.author = author




class Author(Library):
    def __init__(self, name, country, birthday, books):
        super().__init__(name, books)
        self.country = country
        self.birthday = birthday

my_book = Book("Кладовище домашніх тварин", 1983, "Стівен Кінг")
my_book.new_book()
print(my_book)

