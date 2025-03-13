from database import get_session
from models import Case
from datetime import datetime

def add_case():
    session = get_session()

    try:
        print("Enter Case Details")
        name = input("Case name: ")
        description = input("Case description: ")
        status = input("Case status: ")
        client_id = int(input("Client ID: "))
        court_date = input("Court date (YYYY-MM-DD): ")
        event_type = input("Matter Coming up for: ")
        court_name = input("Court name: ")
        judge_name = input("Judge name: ")

        court_date = datetime.strptime(court_date, '%Y-%m-%d').date()

        new_case = Case(
            case_name=name,
            case_description=description,
            status=status,
            client_id=client_id,
            court_date=court_date,
            event_type=event_type,
            court_name=court_name,
            judge_name=judge_name
        )
        session.add(new_case)
        session.commit()
        print("Case added successfully!")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

def update_case():
    session = get_session()
    try:
        case_id = int(input("Case ID to update: "))
        court_date = input("Next court date (YYYY-MM-DD): ")
        event_type = input("Matter to come up for: ")
        court_name = input("New court name: ")
        judge_name = input("New judge name: ")

        court_date = datetime.strptime(court_date, '%Y-%m-%d').date()

        case = session.query(Case).filter_by(id=case_id).first()
        if case:
            case.court_date = court_date
            case.event_type = event_type
            case.court_name = court_name
            case.judge_name = judge_name
            session.commit()
            print("Case updated successfully!")
        else:
            print("Case not found.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

def delete_case():
    session = get_session()
    try:
        case_id = int(input("Case ID to delete: "))
        case = session.query(Case).filter_by(id=case_id).first()
        if case:
            session.delete(case)
            session.commit()
            print("Case deleted successfully!")
        else:
            print("Case not found.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()