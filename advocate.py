from models import Advocate, Case
from database import get_session
def add_advocate():
    session = get_session()
    name=input("Enter Advocate Name: ")
    contact = input("Enter Advocate E-mail: ")

    new_advocate = Advocate(name=name, contact_info= contact)
    session.add(new_advocate)
    session.commit()
    print("Advocate Added Successfully!")

def assign_advocate():
    session = get_session()
    
    case_id= int(input("Enter Case ID: "))
    advocate_id = input("Enter Advocate ID:")
    case = session.query(Case).filter_by(id= case_id).first()
    advocate = session.query(Advocate).filter_by(id=advocate_id).first()
    if case and advocate:
        case.advocates.append(advocate)
        session.commit()
        print ("Advocate Assigned Successfully!")
    else:
        print("No such case or advocate")

def remove_advocate():
    session = get_session()
    try:
        advocate_id = int(input("Advocate ID to remove: "))
        advocate = session.query(Advocate).filter_by(id=advocate_id).first()
        if advocate:
            session.delete(advocate)
            session.commit()
            print("Advocate removed successfully!")
        else:
            print("Advocate not found.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()