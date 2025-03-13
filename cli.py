from close import exit_program
from cases import (add_case, update_case, delete_case)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        
        elif choice == "1":
            add_case()
        elif choice == "2":
            update_case()
        elif choice == "3":
            delete_case()
        
       
        
       
    
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("Welcome to the CMS. "
    "Please select an option:")
    print("0. Exit the program")
   
    print("1. Add Case")
    print("2. Update Case")
    print("3. Delete Case")


if __name__ == "__main__":
    main()
