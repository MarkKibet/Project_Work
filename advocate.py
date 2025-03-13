from models import Advocate
from database import get_session
def add_advocate():
    session = get_session()
    name=input("Enter Advocate Name: ")
    contact = input("Enter Advocate E-mail: ")

    new_advocate = Advocate(name=name, contact_info= contact)
    session.add(new_advocate)
    session.commit()
    print("Advocate Added Successfully!")