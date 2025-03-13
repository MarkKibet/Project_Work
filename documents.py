from database import get_session
from models import Document, Case


def add_document():
    session = get_session()
    try:
        case_id = int(input("Enter case ID of the case: "))
        case = session.query(Case).filter_by(id=case_id).first()
        if not case:
            print ("Case Not Found")
            return
        file = input("Document name: ")
        doc = input("Add file path: ")
        new_doc = Document(description=file, file_path =doc, case_id=case_id)
        session.add(new_doc)
        session.commit()
        print("File added successfully!")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()