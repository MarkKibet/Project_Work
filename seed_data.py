from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from datetime import datetime
from database import get_session
from models import Client, Case, Advocate

class CaseManagementApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.root_layout.add_widget(Label(text="Case Management System", font_size=24))

        buttons = [
            ("Add Client", self.add_client),
            ("Add Case", self.add_case),
            ("Update Case", self.update_case),
            ("Delete Case", self.delete_case),
            ("Add Advocate", self.add_advocate),
            ("Assign Advocate", self.assign_advocate),
            ("Search Cases", self.search_cases),
            ("View Case Details", self.view_case_details),
        ]

        for text, action in buttons:
            btn = Button(text=text, size_hint_y=None, height=50, on_release=action)
            self.root_layout.add_widget(btn)

        return self.root_layout

    # Utility Methods
    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        close_btn = Button(text='Close', size_hint_y=None, height=40)
        popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(400, 300))
        close_btn.bind(on_release=popup.dismiss)
        popup_layout.add_widget(close_btn)
        popup.open()

    def get_input(self, title, hint_text, callback):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        input_field = TextInput(hint_text=hint_text, multiline=False)
        submit_btn = Button(text="Submit", size_hint_y=None, height=40)

        def on_submit(instance):
            user_input = input_field.text.strip()
            if user_input:
                popup.dismiss()
                callback(user_input)
            else:
                self.show_popup("Error", "Input cannot be empty!")

        submit_btn.bind(on_release=on_submit)

        layout.add_widget(input_field)
        layout.add_widget(submit_btn)

        popup = Popup(title=title, content=layout, size_hint=(None, None), size=(400, 300))
        popup.open()

    # Client Management
    def add_client(self, instance):
        def save_client(name):
            self.get_input("Add Client", "Enter contact info", lambda contact: self.save_client_to_db(name, contact))
        self.get_input("Add Client", "Enter client name", save_client)

    def save_client_to_db(self, name, contact):
        session = get_session()
        try:
            new_client = Client(name=name, contact_info=contact)
            session.add(new_client)
            session.commit()
            self.show_popup("Success", "Client added successfully!")
        except Exception as e:
            session.rollback()
            self.show_popup("Error", f"An error occurred: {e}")
        finally:
            session.close()

    # Case Management
    def add_case(self, instance):
        def save_case(name):
            self.get_input("Add Case", "Enter case description", lambda desc:
                self.get_input("Add Case", "Enter case status", lambda status:
                    self.get_input("Add Case", "Enter client ID", lambda client_id:
                        self.get_input("Add Case", "Enter court date (YYYY-MM-DD)", lambda court_date:
                            self.get_input("Add Case", "Enter event_type", lambda event_type:
                                self.get_input("Add Case", "Enter court name", lambda court_name:
                                    self.get_input("Add Case", "Enter judge name", lambda judge_name:
                        
                            self.save_case_to_db(name, desc, status, client_id, court_date, event_type, court_name, judge_name)
                                    )
                            )
                            )
                        )
                    )
                )
            )
        self.get_input("Add Case", "Enter case name", save_case)

    def save_case_to_db(self, name, desc, status, client_id, court_date, event_type, court_name, judge_name):
        try:
            court_date = datetime.strptime(court_date, "%Y-%m-%d").date()
        except ValueError:
            self.show_popup("Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        session = get_session()
        try:
            new_case = Case(case_name=name, case_description=desc, status=status, client_id=client_id, court_date=court_date, event_type=event_type, court_name=court_name, judge_name=judge_name)
            session.add(new_case)
            session.commit()
            self.show_popup("Success", "Case added successfully!")
        except Exception as e:
            session.rollback()
            self.show_popup("Error", f"An error occurred: {e}")
        finally:
            session.close()

    def update_case(self, instance):
        self.get_input("Update Case", "Enter case ID", self.handle_update_case)

    def handle_update_case(self, case_id):
        session = get_session()
        try:
            case = session.query(Case).filter_by(id=case_id).first()
            if not case:
                self.show_popup("Error", "Case not found.")
                return
            def update_event(court_date):
                self.get_input("Update Case", "Enter new court date (YYYY-MM-DD)", lambda court_date: 
                self.get_input("Update Case", "Enter event type", lambda event_type:
                           self.update_case_in_db(case, court_date, event_type))
                           )
            
        finally:
            session.close()

    def update_case_in_db(self, case, court_date, event_type):
        session = get_session()
        try:
            case.court_date = datetime.strptime(court_date, "%Y-%m-%d").date()
            case.event_type= event_type

            session.commit()
            self.show_popup("Success", "Case updated successfully!")
        except Exception as e:
            session.rollback()
            self.show_popup("Error", f"An error occurred: {e}")
        finally:
            session.close()

    def delete_case(self, instance):
        self.get_input("Delete Case", "Enter case ID", self.delete_case_from_db)

    def delete_case_from_db(self, case_id):
        session = get_session()
        try:
            case = session.query(Case).filter_by(id=case_id).first()
            if case:
                session.delete(case)
                session.commit()
                self.show_popup("Success", "Case deleted successfully!")
            else:
                self.show_popup("Warning", "Case not found.")
        except Exception as e:
            session.rollback()
            self.show_popup("Error", f"An error occurred: {e}")
        finally:
            session.close()

    # Advocate Management
    def add_advocate(self, instance):
        def save_advocate(name):
            self.get_input("Add Advocate", "Enter contact info", lambda contact: self.save_advocate_to_db(name, contact))
        self.get_input("Add Advocate", "Enter advocate name", save_advocate)

    def save_advocate_to_db(self, name, contact):
        session = get_session()
        try:
            new_advocate = Advocate(name=name, contact_info=contact)
            session.add(new_advocate)
            session.commit()
            self.show_popup("Success", "Advocate added successfully!")
        except Exception as e:
            session.rollback()
            self.show_popup("Error", f"An error occurred: {e}")
        finally:
            session.close()

    def assign_advocate(self, instance):
        self.get_input("Assign Advocate", "Enter case ID", self.get_case_for_assignment)

    def get_case_for_assignment(self, case_id):
        session = get_session()
        try:
            case = session.query(Case).filter_by(id=case_id).first()
            if case:
                self.get_input("Assign Advocate", "Enter advocate ID", lambda advocate_id: self.assign_advocate_to_case(case_id, advocate_id))
            else:
                self.show_popup("Error", "Case not found.")
        finally:
            session.close()

    def assign_advocate_to_case(self, case_id, advocate_id):
        session = get_session()
        try:
            case = session.query(Case).filter_by(id=case_id).first()
            advocate = session.query(Advocate).filter_by(id=advocate_id).first()
            if case and advocate:
                case.advocates.append(advocate)
                session.commit()
                self.show_popup("Success", "Advocate assigned successfully!")
            else:
                self.show_popup("Error", "Case or Advocate not found.")
        except Exception as e:
            session.rollback()
            self.show_popup("Error", f"An error occurred: {e}")
        finally:
            session.close()

    # Search Cases
    def search_cases(self, instance):
        def search_by_criteria(criteria):
            session = get_session()
            try:
                if criteria == "status":
                    status = self.get_input("Search Cases", "Enter status", lambda status: search_by_status(status))
                elif criteria == "name":
                    name = self.get_input("Search Cases", "Enter case name", lambda name: search_by_name(name))
                elif criteria == "date":
                    date = self.get_input("Search Cases", "Enter court date (YYYY-MM-DD)", lambda date: search_by_date(date))
                elif criteria == "event":
                    event_type = self.get_input("Search Cases", "Enter event type", lambda event_type: search_by_event(event_type))
                elif criteria == "advocate":
                    advocate_name = self.get_input("Search Cases", "Enter advocate name", lambda advocate_name: search_by_advocate(advocate_name))

            except Exception as e:
                self.show_popup("Error", f"An error occurred: {e}")
            finally:
                session.close()

        def search_by_status(status):
            session = get_session()
            try:
                cases = session.query(Case).filter_by(status=status).all()
                self.display_search_results(cases)
            finally:
                session.close()

        def search_by_name(name):
            session = get_session()
            try:
                cases = session.query(Case).filter(Case.case_name.ilike(f"%{name}%")).all()
                self.display_search_results(cases)
            finally:
                session.close()

        def search_by_date(date):
            session = get_session()
            try:
                court_date = datetime.strptime(date, "%Y-%m-%d").date()
                cases = session.query(Case).filter_by(court_date=court_date).all()
                self.display_search_results(cases)
            finally:
                session.close()

        def search_by_event(event_type):
            session = get_session()
            try:
                cases = session.query(Case).filter_by(event_type=event_type).all()
                self.display_search_results(cases)
            finally:
                session.close()

        def search_by_advocate(advocate_name):
            session = get_session()
            try:
                advocate = session.query(Advocate).filter(Advocate.name.ilike(f"%{advocate_name}%")).first()
                if advocate:
                    cases = session.query(Case).filter(Case.advocates.any(id=advocate.id)).all()
                    self.display_search_results(cases)
                else:
                    self.show_popup("Warning", "No advocate found with that name.")
            finally:
                session.close()

        self.get_input("Search Cases", "Search by (status/name/date/event/advocate)", search_by_criteria)

    def display_search_results(self, cases):
        if not cases:
            self.show_popup("Info", "No cases found matching the criteria.")
            return

        result = "\n".join([f"ID: {case.id}, Name: {case.case_name}, Status: {case.status}" for case in cases])
        self.show_popup("Search Results", result)

    # View Case Details
    def view_case_details(self, instance):
        self.get_input("View Case Details", "Enter case ID", self.show_case_details)

    def show_case_details(self, case_id):
        session = get_session()
        try:
            case = session.query(Case).filter_by(id=case_id).first()
            if case:
                details = (f"ID: {case.id}\nName: {case.case_name}\nDescription: {case.case_description}\n"
                           f"Status: {case.status}\nCourt Date: {case.court_date}\nEvent Type: {case.event_type}\n"
                           f"Court Name: {case.court_name}\nJudge Name: {case.judge_name}\n"
                           f"Advocates: {', '.join([advocate.name for advocate in case.advocates])}")
                self.show_popup("Case Details", details)
            else:
                self.show_popup("Warning", "Case not found.")
        except Exception as e:
            self.show_popup("Error", f"An error occurred: {e}")
        finally:
            session.close()

if __name__ == "__main__":
    CaseManagementApp().run()
