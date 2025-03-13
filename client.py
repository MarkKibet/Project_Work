from models import Client
from database import get_session

def add_client():
    session = get_session()
    print ("Enter Client Details ")
    name = input("Enter Client Name: ")
    contact =input("Enter Client mail: ")

    new_client= Client(name=name, contact_info=contact)
    session.add(new_client)
    session.commit()
    print ("Client added successfuly!")


