from models import Book
from library import Library

library = Library()
library.load_books()

print("~~~~~ Welcome to Our Library ~~~~~")
#Main logic
while True:
    
    print()
    print("1. View Books")
    print("2. Add Books")
    print("3. Search Books")
    print("4. Borrow Books")
    print("5. Return Books")
    print("6. Delete Books")
    print("7. Exit")
    print()

    try:
        user_input = int(input("Choose a Number to Get Started: "))
        print()

        if 1 <= user_input <= 7: 

            #Check the list of books
            if user_input == 1:

                books = library.list_books()

                if not books:
                    print("Currently No Books are Available")
                    print()
                else:
                    print("Available Books:")
                    for book in books:
                        print(book)

            #Exit from the program
            elif user_input == 7:
                print("~~~~~ Thanks For Using Our Library Program ~~~~~")
                break

            #Add books
            elif user_input == 2:

                while True:
                    try:
                        number_of_books = int(input("How Many Books Do You Want to Add: "))

                        if number_of_books <= 0:
                            print("Wrong Input! Please Put a Valid Number!")
        
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
                                    print(f"Book was Added Successfully: Book ID: {book_id}, Book Title: {book_title}, Book Author: {book_author}")
                                    print()
                                else:
                                    print()
                                    print(f"Duplicate Book: Book ID: {book_id}, Book Title: {book_title}, Book Author: {book_author}")
                            break  
                    
                    except ValueError:
                        print("Wrong Input! Please Pick a Number.")  

            #Search books
            elif user_input == 3:
                
                print("1. Search by ID")
                print("2. Search by Book Title")
                print("3. Search by Author")
                print()

                while True:
                    try:
                        search = int(input("Pick Your Search Method: "))
                        if 1 <= search <= 3:

                            #search by ID
                            if search == 1:
                                book_id = input("Enter the Book ID: ")
                                search_id = library.book_search_by_id(book_id)

                                if search_id:
                                    print(f"Book Found: {search_id}")
                                else:
                                    print("Book Not Found!")
                                break
                            
                            #Search by Title
                            elif search == 2:
                                book_title = input("Enter the Book Title: ")
                                search_title = library.book_search_by_title(book_title)

                                if not search_title:
                                    print("Book Not Found!")
                                else:
                                    print("Books Found:")
                                    for book in search_title:
                                        print(book)
                                break

                            #Search by Author
                            else:
                                author_name = input("Enter the Book Author: ")
                                search_author = library.book_search_by_author(author_name)

                                if not search_author:
                                    print("Book Not Found!")
                                else:
                                    print("Books Found:")
                                    for book in search_author:
                                        print(book)
                                break

                        else:
                            print("Please Pick a Valid Search Method!")

                    except ValueError:
                        print("Choose Between 1, 2, and 3")
            #Borrow Book
            elif user_input == 4:

                book_id_to_borrow = input("Enter the Book ID: ")
                borrow = library.borrow_book(book_id_to_borrow)

                if borrow is None:
                    print("Book was Not Found! Please Enter a Valid Book ID")
                elif borrow:
                    library.save_books()
                    print("Borrowed Successfully.")
                elif borrow is False:
                    print("Book is Already Borrowed.")

            #Return Book
            elif user_input == 5:

                book_id_to_return = input("Enter the Book ID: ")
                returned = library.return_book(book_id_to_return)

                if returned is None:
                    print("Book was Not Found! Please Enter a Valid Book ID")
                elif returned:
                    library.save_books()
                    print("Book Returned Successfully.")
                elif returned is False:
                    print("Book is Already Available (Not Borrowed)")

            #Delete Book
            elif user_input == 6:

                book_to_delete = input("Enter the Book ID You Want to Remove: ")
                deleted = library.delete_book(book_to_delete)

                if deleted:
                    library.save_books()
                    print("Book was Deleted Successfully")
                else:
                    print("Book was not Found!")


        else:
            print("Wrong Input! Please Pick a Number Between 1 and 7")
            print()

    except ValueError:
        print()
        print("Wrong Input! Please a Pick Number Between 1 and  7")
        print()

    

