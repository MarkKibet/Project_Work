from database import get_session
from models import Case, Advocate
from datetime import datetime

def search_cases():
    session = get_session()
    try:
        print("Select a search criteria:")
        print("1. Status")
        print("2. Case Name")
        print("3. Next Court Date")
        print("4. Event Type")
        print("5. Advocate Name")
        choice = input("Enter your choice: ")

        if choice == "1":
            status = input("Status of the cases to search for: ")
            cases = session.query(Case).filter_by(status=status).all()
        elif choice == "2":
            name = input("Name of the case to search for: ")
            cases = session.query(Case).filter(Case.case_name.ilike(f"%{name}%")).all()
        elif choice == "3":
            next_date = input("Next court date (YYYY-MM-DD) to search for: ")
            next_date = datetime.strptime(next_date, '%Y-%m-%d').date()
            cases = session.query(Case).filter_by(court_date=next_date).all()
        elif choice == "4":
            event_type = input("Event type to search for: ")
            cases = session.query(Case).filter_by(event_type=event_type).all()
        elif choice == "5":
            advocate_name = input("Name of the advocate to search for: ")
            advocate = session.query(Advocate).filter(Advocate.name.ilike(f"%{advocate_name}%")).first()
            if advocate:
                cases = session.query(Case).filter(Case.advocates.any(id=advocate.id)).all()
            else:
                print("No advocate found with that name.")
                return
        else:
            print("Invalid choice.")
            return

        if not cases:
            print("No cases found matching the criteria.")
            return

        print("Cases matching the criteria:")
        for case in cases:
            advocates = ", ".join([advocate.name for advocate in case.advocates])
            print(f"Case ID: {case.id}, Name: {case.case_name}, Status: {case.status}, Court Date: {case.court_date}, Event Type: {case.event_type}, Advocates: {advocates}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
