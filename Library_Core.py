class LibraryItem:
    def __init__(self, id: int, title: str, author: str, genre: str, price: float, availiability: bool):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__genre = genre 
        self.__price = price
        self.__availiability = availiability
    def get_info(self):
        pass
    def borrow(self):
        pass
    def return_item():
        pass
class Book:
    def __init__(self, pages: int):
        self.__pages = pages
    def get_info(self):
        pass
    def borrow(self):
        pass
    def return_item():
        pass
class Magazine:
    def __init__(self, issue_number: int):
        self.__issue_number = issue_number
    def get_info(self):
        pass
    def borrow(self):
        pass
    def return_item():
        pass
class User:
    def __init__(self, id: int, name: str, borrowed_items: list):
        self.__id = id
        self.__name = name
        self.__borrowed_items = borrowed_items
    def borrow_item(self):
        pass
    def return_item(self):
        pass
    def can_borrow(self):
class NormalUser:
    def __init__(self):
        self.__max_borrow = 3
    def can_borrow(self):
        pass
class PremiumUser:
    def __init__(self):
        self.__max_borrow = 10
    def can_borrow(self):
        pass
class Library:
    def __init__(self, name: str, collection: list, users: list):
        self.__name = name
        self.__collection = collection
        self.__users = users
    def add_item(self, item):
        pass
    def remove_item(self, id):
        pass
    def search(self, title):
        pass
    def save_to_json(self, file):
        pass
    def load_from_json(self, file):
        pass
