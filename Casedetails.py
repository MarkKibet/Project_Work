from models import CaseDetails, Case
from database import get_session
def add_case_details():
    session = get_session()
    try:
        case_id = int(input("Enter the Case ID to add details to: "))

        case = session.query(Case).filter_by(id=case_id).first()
        if not case:
            print("Case not found.")
            return

        summary = input("Summary of the case: ")
        agreed_fee = input("Legal Fee: ")

        case_detail = CaseDetails(
            Summary=summary,
            agreed_fee=agreed_fee,
            case_id=case_id,

        )

        # Add the new case details to the session and commit
        session.add(case_detail)
        session.commit()
        print("Case Details added successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number for Case ID.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

def update_case_details():
    session = get_session()
    casedetails_id = int(input("Enter Case Details ID: "))
    agreed_fee= input("Update the Legal Fee: ")

    detail = session.query(CaseDetails).filter_by(id=casedetails_id).first()
    if detail:
        detail.agreed_fee= agreed_fee
        session.commit()
        print ("Legal Fee Updated")
    else:
        print("No such case details")

