import json
from models import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                return False
    
        self.books.append(book)
        return True
 
    def list_books(self):
        return self.books
    
    def book_search_by_id(self, id_of_the_book):
        for existing_book in self.books:
            if existing_book.book_id == id_of_the_book:
                return existing_book
        return None
    
    def book_search_by_title(self, title):
        matched_books_title = []

        for existing_book in self.books:
            if existing_book.title.lower().strip() == title.lower().strip():
                matched_books_title.append(existing_book)
        return matched_books_title
   
    def book_search_by_author(self, author_name):
        matched_books_author = []

        for existing_book in self.books:
            if existing_book.author.lower().strip() == author_name.lower().strip():
                matched_books_author.append(existing_book)
        return matched_books_author
    
    def borrow_book(self, book_id):
        for existing_book in self.books:
            if existing_book.book_id == book_id:
                if existing_book.available:
                    existing_book.available = False
                    return True
                else:
                    return False
        return None
    
    def return_book(self, book_id):
        for existing_book in self.books:
            if existing_book.book_id == book_id:
                if not existing_book.available:
                    existing_book.available = True
                    return True
                else:
                    return False
        return None
    
    def delete_book(self, book_id):
        for existing_book in self.books:
            if existing_book.book_id == book_id:
                self.books.remove(existing_book)
                return True
        return False
    
    def load_books(self):

        try:
            with open("book.json", "r") as file:
                data = json.load(file)
                books = []

            for book in data:
                book_data = Book(book["book_id"], book["title"], book["author"], book["available"])
                books.append(book_data)

        except FileNotFoundError:
            print("Book not Found!")
            books = []

        self.books = books

    def save_books(self):

        book_list = []

        for book in self.books:
            book_info = {"book_id": book.book_id, 
                         "title": book.title,
                         "author": book.author,
                         "available": book.available} 
            
            book_list.append(book_info)
        
        with open("book.json", "w") as file:   
            json.dump(book_list, file, indent=4)



        
            






    
        
