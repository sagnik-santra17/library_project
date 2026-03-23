class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Availability: {self.get_status()}"
    
    def get_status(self):
        return "Available" if self.available else "Borrowed"
        
