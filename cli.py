from close import exit_program
from cases import (add_case, update_case, delete_case)
from client import add_client
from advocate import add_advocate


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_client()
        
        elif choice == "2":
            add_case()
        elif choice == "3":
            update_case()
        elif choice == "4":
            delete_case()
        elif choice == "5":
            add_advocate()
        
        
       
        
       
    
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("Welcome to the CMS. "
    "Please select an option:")
    print("0. Exit the program")
    print("1. Add Client ")
   
    print("2. Add Case")
    print("3. Update Case")
    print("4. Delete Case")
    print("5. Add Advocate")
  


if __name__ == "__main__":
    main()
