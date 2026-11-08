

class Book:
    total_books:int = 0
    def __init__(self,title:str,author:str,copies:int) -> None:
        if copies < 1:
            raise ValueError("copies must be at least 1")
        self.__title = title
        self.__author = author
        self.__copies = copies
        self.__available:int = copies
        Book.total_books = Book.total_books + 1

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author


    @property
    def copies(self):
        return self.__copies

    @property
    def available(self)->int: 
        return self.__available

    def is_available(self)->bool:
        return self.__available > 0
   
    def borrow(self):
        if not self.is_available():
            raise ValueError("copies must be at least 1")
        self.__available = self.__available - 1

    def return_book(self):
        if self.available == self.copies:
            raise ValueError("All copies are already in the library!")
        self.__available = self.__available + 1
    
    
    def __str__(self)->str:
        return (self.title + " by " + self.author + " ("
                + str(self.available) + "/" + str(self.copies) + " available)")




