from library import Library

library = Library()

#Valid input check
def valid_input_check(prompt, min, max):
    
    while True:
        try:
            user_input = int(input(prompt))

            if min <= user_input <= max:
                return user_input
            else:
                print(f"Invalid input ❌. Please choose again between {min} and {max} 🔢")

        except ValueError:
            print("Invalid Input ❌. Please Pick a Valid Number 🔢")


#Search again or main menu function:
def search_again_and_main_menu():

        print()
        next_action = valid_input_check("Enter 1 to Search Again/Enter 2 to Go to the Main Menu: ", 1, 2)

        if next_action == 1:

            print()
            print("----- 🔎 Search Menu 🔍 -----")
            print()
            print("1. Search by ID ℹ️")
            print("2. Search by Book Title ✍🏻")
            print("3. Search by Author 🙇🏻")
            print()
            print("------------------------------")
            print()
            return next_action
        
        elif next_action == 2:
            return next_action
        


def search_borrow_main_menu():
    
    print()
    print("Choose action 👈")
    print("1. Borrow 👍🏻")
    print("2. Search Again 🔍")
    print("3. Main Menu ℹ️")

    print()
    next_action = valid_input_check("Pick: ", 1, 3)
    

    if next_action == 1:
        return next_action
        
    elif next_action == 2:
        print()
        print("----- 🔎 Search Menu 🔍 -----")
        print()
        print("1. Search by ID ℹ️")
        print("2. Search by Book Title ✍🏻")
        print("3. Search by Author 🙇🏻")
        print()
        print("------------------------------")
        print()

        return next_action
    
    elif next_action == 3:
        return next_action

