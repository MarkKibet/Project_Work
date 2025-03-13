from close import exit_program
from cases import (add_case, update_case, delete_case)
from client import add_client
from advocate import add_advocate, assign_advocate, remove_advocate
from Casedetails import add_case_details, update_case_details
from search import search_cases
from documents import add_document
from view import view_case_details



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
            add_document()
        elif choice == "5":
            delete_case()
        elif choice == "6":
            add_advocate()
        elif choice == "7":
            assign_advocate()
        elif choice == "8":
            remove_advocate()
        elif choice == "9":
            add_case_details()
        elif choice == "10":
            update_case_details()
        elif choice == "11":
            search_cases()
        elif choice == "12":
            view_case_details()
        
        
       
              
         
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("Welcome to the CMS. "
    "Please select an option:")
    print("0. Exit the program")
    print("1. Add Client ")
    print("2. Add Case")
    print("3. Update Case")
    print("4. Add Document")
    print("5. Delete Case")
    print("6. Add Advocate")
    print("7. Assign Advocate")
    print("8. Remove Advocate")
    print("9. Add Case Details")
    print("10. Update Legal Fee Payment")
    print("11. Search Case")
    print("12. View Case Details")
  


if __name__ == "__main__":
    main()
