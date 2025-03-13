from database import get_session
from models import Case



def view_case_details():
    session = get_session()
    try:
        case_id = int(input("Case ID to view details: "))
        case = session.query(Case).filter_by(id=case_id).first()
        if case:
            advocates = ", ".join([advocate.name for advocate in case.advocates])
            print(f"Case ID: {case.id}")
            print(f"Case Name: {case.case_name}")
            print(f"Description: {case.case_description}")
            print(f"Status: {case.status}")
            print(f"Court Date: {case.court_date}")
            print(f"Event Type: {case.event_type}")
            print(f"Court Name: {case.court_name}")
            print(f"Before: {case.judge_name}")
            print(f"Advocates: {advocates}")
        else:
            print("Case not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
