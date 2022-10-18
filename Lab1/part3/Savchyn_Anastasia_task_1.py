class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Name should be a string")
        elif len(val) < 2:
            return ValueError("You should enter a name > 2 characters")
        self.__name = val

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Name should be a string")
        elif len(val) < 2:
            return ValueError("You should enter a surname > 2 characters")
        self.__surname = val

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book:
    def __init__(self, author, title, publisher, year):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        if not val or not isinstance(val, Author):
            raise TypeError("Author should be an instance of class Author")
        self.__author = val

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Title should be a string")
        self.__title = val

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Publisher should be a string")
        self.__publisher = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Year should be an integer value")
        self.__year = val


class Library:
    # __BOOKS = []

    def __init__(self):
        self.__BOOKS = []

    # @property
    # def book(self):
    #     return self.__book

    # @book.setter
    # def book(self, val):
    #     if not val or not isinstance(val, Book):
    #         raise TypeError("Book should be an instance of class Book")
    #     self.__book = val
    #     # self.add(self, self.book)

    def add(self, book):
        if not book or not isinstance(book, Book):
            raise TypeError("Book should be an instance of class Book")
        elif book in self.__BOOKS:
            raise ValueError("Book is already added")
        self.__BOOKS.append(book)

    def delete(self, book):
        if not book or not isinstance(book, Book):
            raise TypeError("Book should be an instance of class Book")
        if book not in self.__BOOKS:
            raise ValueError("There is no such book in library")
        self.__BOOKS.remove(book)

    def search_by_surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname must be a string")
        result = []
        for book in self.__BOOKS:
            if book.author.surname == surname:
                result.append(book.title)
        if not result:
            raise ValueError("Sorry, there is no such books")
        return result

    def search_by_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        result = []
        for book in self.__BOOKS:
            if book.title == title:
                result.append(book.title)
        if not result:
            raise ValueError("Sorry, there is no such books")
        return result

    def search_by_year(self, year):
        if not isinstance(year, int):
            raise TypeError("Year should be an integer")
        result = []
        for book in self.__BOOKS:
            if book.year == year:
                result.append(book.title)
        if not result:
            raise ValueError("Sorry, there is no such books")
        return result

    def __str__(self):
        books_str = ''
        for book in self.__BOOKS:
            books_str += f'{book.title} - {book.author}\n'
        return books_str


def main():
    try:
        author1 = Author("Den", "Smith")
        author2 = Author("Coley", "Brown")

        book1 = Book(author1, "Wind as a person", "BookClub", 2016)
        book2 = Book(author1, "Silence", "BookClub", 2000)
        book3 = Book(author2, "Winter Romance", "BookClub", 1990)

        library = Library()
        library.add(book1)
        library.add(book2)
        library.add(book3)

        print(library)

        library.delete(book3)

        print(library)

        print(library.search_by_year(2000))
        print(library.search_by_title("Wind as a person"))
        print(library.search_by_surname("Smith"))

    except ValueError as e:
        print(str(e))
    except TypeError as e:
        print(str(e))


if __name__ == "__main__":
    main()


