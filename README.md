The Case Management System Backend is a robust solution designed to manage legal cases, clients, and advocates. This system allows users to add, update, delete, and search for cases, as well as assign advocates to cases.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Graphical User Interface (GUI)](#graphical-user-interface-gui)
- [Database Setup](#database-setup)

## Features

- **Case Management**: Add, update, delete, and search cases.
- **Client Management**: Add and manage clients associated with cases.
- **Advocate Management**: Add advocates and assign them to cases.
- **Search Functionality**: Search cases by status, name, court date, event type, and advocate.
- **CLI and GUI**: Provides both command-line and graphical user interfaces.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone 
   cd Project_Work
2. Set Up a Virtual Environment:
   
   


python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
Install Dependencies



Database Setup:

Ensure you have SQLite installed. The application uses SQLite for simplicity, but you can configure it to use other databases like PostgreSQL or MySQL.
Run the following command to set up the database:

python database.py
Usage
Command-Line Interface (CLI)
Run the CLI:

python cli.py
CLI Commands:

Add Client: Add a new client to the system.
Add Case: Add a new case associated with a client.
Update Case: Update the details of an existing case.
Delete Case: Delete a case from the system.
Add Advocate: Add a new advocate to the system.
Assign Advocate: Assign an advocate to a case.
Remove Advocate.
Search Cases: Search for cases based on various criteria.
View Case Details: View detailed information about a specific case.
Graphical User Interface (GUI)

Run the GUI:
python seed_data.py
GUI Interface:

The GUI provides a user-friendly interface to perform the same operations as the CLI.
Use the buttons and input fields to manage clients, cases, and advocates.
Database Setup
The database schema is defined using SQLAlchemy ORM.
Models include Client, Case, Advocate, Document and CaseDetails.
Relationships are defined to manage associations between clients, cases, and advocates.
