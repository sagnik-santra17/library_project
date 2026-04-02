from models import Book
from library import Library
import utils

library = Library()
library.load_books()
print()
print("----- 📚⭐📚⭐📚 Welcome to Our Library 📚⭐📚⭐📚 -----")

def view_books(): #Check the list of books

    books = library.list_books()

    if not books:
        print("Currently No Books are Available ❌")
        print()
    else:
        print("-----------------------")
        print("Available Books 📚👇🏻:")
        print("-----------------------")
        print()
        for book in books:
            print(book)
            print()
            print("-----------------------")
            print()
    


def exit_program(): #Exit from the program

    print()
    print("----- 📚⭐📚⭐📚 Thanks For Using Our Library Program 📚⭐📚⭐📚 -----")
    print()


def add_books(): #Add books

    while True:
        try:
            number_of_books = int(input("How Many Books Do You Want to Add: "))

            if number_of_books <= 0:
                print("Invalid input ❌. Please enter a valid number 🔢")

            else:
                for _ in range(number_of_books):

                    book_id = input("Enter the Book's ID: ")
                    book_title = input("Enter the Book's Title: ")
                    book_author = input("Enter the Book's Author: ")

                    book = Book(book_id, book_title, book_author)
                    added_book = library.add_book(book)
                    
                    #Checks for duplicate book entry
                    if added_book:
                        print()
                        library.save_books()
                        print(f"Book added successfully ✅: Book ID: {book_id}, Book Title: {book_title}, Book Author: {book_author}")
                        print()
                    else:
                        print()
                        print(f"Duplicate book found ⚠️: Book ID: {book_id}, Book Title: {book_title}, Book Author: {book_author}")
                break  
        
        except ValueError:
            print("Invalid input ❌. Please enter a number 🔢")  


def search_books(): #Search books

    print()
    print("----- 🔎 Search Menu 🔍 -----")
    print()
    print("1. Search by ID ℹ️")
    print("2. Search by Book Title ✍🏻")
    print("3. Search by Author 🙇🏻")
    print()
    print("------------------------------")
    print()
    

    while True:

        print()
        search = utils.valid_input_check("Pick Your Search Method: ", 1, 3)

        #search by ID
        if search == 1:
            book_id = input("Enter the Book ID: ")
            print()
            search_id = library.book_search_by_id(book_id)

            if search_id:
                print(f"Book Found ✅\n{search_id}")
                print("------------------------------")
            else:
                print("Book Not Found! ❌")
                print()
        
        #Search by Title
        elif search == 2:
            book_title = input("Enter the Book Title: ")
            print()
            search_title = library.book_search_by_title(book_title)

            if not search_title:
                print("Book Not Found ❌")
            else:
                print("Books Found ✅")
                for book in search_title:
                    print(book)
                    print("------------------------------")
            
        #Search by Author
        else:
            author_name = input("Enter the Book Author: ")
            print()
            search_author = library.book_search_by_author(author_name)

            if not search_author:
                print("Book Not Found ❌")
            else:
                print("Matching books found ✅")
                for book in search_author:
                    print(book)
                    print("------------------------------")
        
        next_action = utils.search_borrow_main_menu()

        if next_action == 1:

            borrow_book()
            main_menu_action = utils.search_again_and_main_menu()

            if main_menu_action == 1:
                continue
            elif main_menu_action == 2:
                break

        elif next_action == 2:
            continue
            
        elif next_action == 3:
            break
        

def borrow_book(): #Borrow Book

    book_id_to_borrow = input("Enter the Book ID: ")
    borrow = library.borrow_book(book_id_to_borrow)

    if borrow is None:
        print("Book not found ❌. Please enter a valid book ID 🆔")
    elif borrow:
        library.save_books()
        print("Book borrowed successfully ✅")
    elif borrow is False:
        print("This book is already borrowed 📕")

def return_book(): #Return Book

    book_id_to_return = input("Enter the Book ID: ")
    returned = library.return_book(book_id_to_return)

    if returned is None:
        print("Book was Not Found ❌! Please Enter a Valid Book ID 👈")
    elif returned:
        library.save_books()
        print("Book returned successfully ✅")
    elif returned is False:
        print("This book is already available 📗")


def delete_book(): #Delete Book

    book_to_delete = input("Enter the Book ID You Want to Remove: ")
    deleted = library.delete_book(book_to_delete)

    if deleted:
        library.save_books()
        print("Book deleted successfully 🗑️")
    else:
        print("Book not Found ❌")



while True:
    
    print()
    print("----- 📚 MAIN MENU 📚 -----")
    print()
    print("1. View Books 📚")
    print("2. Add Books ➕")
    print("3. Search Books 🔍")
    print("4. Borrow Books 👍")
    print("5. Return Books 👈")
    print("6. Delete Books 🗑️")
    print("7. Exit 👍🏻")
    print()
    print("---------------------")
    print()


    user_input = utils.valid_input_check("Choose a Number to Get Started: ", 1, 7)
    print()

    if 1 <= user_input <=7:
        if user_input == 1:
            view_books()
        
        elif user_input == 7:
            exit_program()
            break

        elif user_input == 2:
            add_books()

        elif user_input == 3:
            search_books()
        
        elif user_input == 4:
            borrow_book()

        elif user_input == 5:
            return_book()
        
        elif user_input == 6:
            delete_book()
