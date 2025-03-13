The Case Management System Backend is a powerful tool designed to streamline the management of legal cases, clients, and advocates. It supports essential features like adding, updating, deleting, and searching for cases, alongside seamless advocate assignment.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Graphical User Interface (GUI)](#graphical-user-interface-gui)
- [Database Setup](#database-setup)
- [Database Schema](#database-schema)

## Features

- **Case Management**: Add, update, delete, and search cases.
- **Client Management**: Add, update, and delete client records.
- **Advocate Management**: Add advocates, assign them to cases, and remove them.
- **Document Management**: Upload and manage case-related documents.
- **Case Details & Payments**: Add case details and manage fee payments.
- **Search Functionality**: Search by case status, client name, court date, event type, or advocate.
- **Dual Interface**: Use either the command-line or GUI for flexibility.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:MarkKibet/Project_Work.git

   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  
   ```

3. **Install Dependencies**:
   ```bash
   pip install kivy
   ```

## Database Setup

Ensure SQLite is installed 
   ```bash
   python database.py
   ```

## Usage

### Command-Line Interface (CLI)

Run the CLI to manage cases, clients, and other operations:
   ```bash
   python cli.py
   ```

Available Commands:
- **Exiting the System**: Exit the CSM.
- **Add Client**: Register a new client.
- **Add Case**: Create a new case.
- **Update Case**: Modify existing case details.
- **Delete Case**: Remove a case.
- **Add Advocate**: Add a new advocate.
- **Add Document**: Add a new document related the case.
- **Assign Advocate**: Link an advocate to a case.
- **Remove Advocate**: Unlink an advocate from a case.
- **Search Cases**: Filter cases by multiple criteria.
- **View Case Details**: See complete case information.

### Graphical User Interface (GUI)

Launch the GUI for an intuitive, visual experience:
   ```bash
   python seed_data.py
   ```

Navigate through clients, cases, and advocates with ease via buttons and input fields.(This was an esperiment, I tried tkinter first: was a bit complicated, settled on Kivy: which I have used )

## Database Schema

The database structure is built with SQLAlchemy ORM, including models for:
- **Client**
- **Case**
- **Advocate**
- **Document**
- **CaseDetails**
