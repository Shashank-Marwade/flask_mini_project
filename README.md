# Employee Management System

This project is a simple web-based Employee Management System built using Flask and SQLAlchemy. It allows for managing employee details such as adding, updating, deleting, and querying employee records based on their salaries.

## Features

- **Add Employee**: Input employee name, salary, and phone number to add them to the database.
- **Delete Employee**: Remove employee records from the system.
- **Update Employee**: Modify existing employee details.
- **Query Salaries**: Find the N-th highest salary among employees.

## Technologies Used

- **Flask**: A micro web framework written in Python.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy.
- **SQLite**: A C library that provides a lightweight disk-based database.

## Setup and Installation

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python installed on your machine. This application is built using Python 3.8. Download it from [python.org](https://www.python.org/downloads/) if it's not installed.

### Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://your-github-repo-url.git
cd path-to-your-project-folder
```

### Step 2: Create a Virtual Environment

(Optional but recommended) Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python modules with pip:

```bash
pip install Flask SQLAlchemy
```

### Step 4: Initialize the Database

Uncomment the line # db.create_all() in your code to create the initial database. Comment it back once the database is created to avoid recreating the database every time you run the application.

### Step 5: Run the Application

Start the server using the following command:

```bash
python app.py
```

### Usage

Navigate through the application using the interface provided:

Add new employees using the form.
Update or delete existing employees by clicking on the respective links next to each employee.
Use the 'Find N-th Highest Salary' feature by inputting a number into the form.

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.
