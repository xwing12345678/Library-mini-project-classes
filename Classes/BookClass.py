

class Book:
    total_books:int = 0
    def __init__(self,title:str,author:str,copies:int) -> None:
        if copies < 1:
            raise ValueError("copies must be at least 1")
        self.title = title
        self.author = author
        self.copies = copies
        self.available = copies
        Book.total_books = Book.total_books + 1

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title:str):
        self.__title = title

    @title.getter
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author:str):
        self.__author = author

    @author.getter
    def author(self):
        return self.__author

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, copies:int):
        self.__copies = copies

    @copies.getter
    def copies(self):
        return self.__copies



