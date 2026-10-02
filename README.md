# Student Management & Result Analysis System

A Python-based Student Management and Result Analysis System for managing student records, academic marks, and class-level performance analysis.

This project demonstrates practical Python programming, Object-Oriented Programming, modular programming, CRUD operations, JSON file handling, exception handling, sorting, filtering, and basic data analysis.

## Overview

The application provides a command-line interface for managing student information and academic performance.

It allows users to:

* Add and manage student records
* Add, update, and remove subject marks
* Calculate total and average marks
* Generate grades
* Determine pass or fail status
* Search students
* Sort students by performance
* Filter students
* Perform subject-wise analysis
* Calculate class statistics
* Identify the class topper
* Store data persistently using JSON

## Features

### Student Management

* Add new students
* View all students
* Search students by Student ID
* Update student information
* Delete student records

### Result Management

* Add subject marks
* Update existing marks
* Remove subject marks
* Calculate total marks
* Calculate average marks
* Generate grades
* Determine pass/fail status

### Data Analysis

* Sort students by name
* Sort students by total marks
* Sort students by average marks
* Filter students based on performance
* Calculate subject-wise average
* Find highest marks in each subject
* Find lowest marks in each subject
* Calculate class average
* Identify the class topper

### Data Persistence

Student records are stored in a JSON file.

The application automatically loads existing student data when it starts and saves changes to the JSON file.

## Technology Stack

| Technology                  | Purpose                          |
| --------------------------- | -------------------------------- |
| Python 3                    | Core programming language        |
| JSON                        | Data persistence                 |
| File Handling               | Reading and writing student data |
| Object-Oriented Programming | Student data modelling           |
| Standard Python Library     | Application functionality        |

## Project Structure

```text
Student-Management-System/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── student.py
│   ├── result.py
│   ├── file_manager.py
│   └── utils.py
│
├── data/
│   └── students.json
│
├── .gitignore
├── README.md
└── requirements.txt
```

## File Description

| File                  | Description                                     |
| --------------------- | ----------------------------------------------- |
| `app/main.py`         | Main application entry point and CLI menu       |
| `app/student.py`      | Student class and student-related operations    |
| `app/result.py`       | Result calculations and statistical analysis    |
| `app/file_manager.py` | JSON data loading and saving                    |
| `app/utils.py`        | Input validation and reusable utility functions |
| `app/__init__.py`     | Makes the app directory a Python package        |
| `data/students.json`  | Persistent student data                         |
| `.gitignore`          | Files excluded from version control             |
| `requirements.txt`    | Project dependency information                  |
| `README.md`           | Project documentation                           |

## Application Flow

```text
Start Application
       |
       v
Load Student Data
       |
       v
Display Main Menu
       |
       +---- Add Student
       |
       +---- View Students
       |
       +---- Search Student
       |
       +---- Update Student
       |
       +---- Delete Student
       |
       +---- Manage Marks
       |
       +---- Sort / Filter
       |
       +---- Result Analysis
       |
       v
Save Updated Data
       |
       v
Exit
```

## Result Calculation

The system calculates total and average marks using the subjects recorded for each student.

### Grading Criteria

| Average Marks | Grade |
| ------------: | :---- |
|        90–100 | A+    |
|         80–89 | A     |
|         70–79 | B     |
|         60–69 | C     |
|         50–59 | D     |
|         40–49 | E     |
|      Below 40 | F     |

A student is considered `PASS` when the student has marks of at least 40 in every recorded subject.

## Example

```text
Student ID : S001
Name       : Test Student
Age        : 20
Department : CSE

Marks:
Python : 95
DBMS   : 85
OS     : 88
Math   : 90

Total   : 358
Average : 89.50
Grade   : A
Result  : PASS
```

## Installation and Setup

### Prerequisites

* Python 3.x
* Git
* Visual Studio Code or another code editor

### Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Navigate to the Project

```bash
cd Student-Management-System
```

### Run the Application

Run the application from the project root directory:

```bash
python -m app.main
```

## Main Menu

```text
========================================
     STUDENT MANAGEMENT SYSTEM
========================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Add / Update Marks
7. Remove Marks
8. Sort Students
9. Filter Students
10. Subject-wise Analysis
11. Class Statistics
12. Exit
```

## Python Concepts Demonstrated

This project provides practical implementation of:

* Variables and data types
* Strings and numeric operations
* Conditional statements
* `for` loops
* `while` loops
* Functions
* Function parameters
* Return values
* Lists
* Dictionaries
* Sets
* List comprehensions
* Lambda functions
* Sorting
* Filtering
* Exception handling
* File handling
* JSON serialization
* JSON deserialization
* Classes and objects
* Constructors
* Instance methods
* Class methods
* Object-to-dictionary conversion
* Modular programming
* CRUD operations
* Basic data analysis

## Object-Oriented Programming

The project uses a `Student` class to represent student records.

Each student object contains:

* Student ID
* Name
* Age
* Department
* Subject marks

The class also provides methods for:

* Adding marks
* Updating marks
* Removing marks
* Calculating total marks
* Calculating average marks
* Generating grades
* Checking pass/fail status
* Converting objects to dictionaries
* Creating objects from dictionaries

## Architecture

The application follows a modular architecture:

```text
                    main.py
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
    student.py     result.py     file_manager.py
                                      |
                                      v
                              students.json

                       |
                       v
                    utils.py
```

Each module has a specific responsibility, making the application easier to understand, maintain, and extend.

## Data Storage

The application uses JSON-based persistence.

Example:

```json
[
    {
        "student_id": "S001",
        "name": "Test Student",
        "age": 20,
        "department": "CSE",
        "marks": {
            "Python": 95,
            "DBMS": 85,
            "OS": 88,
            "Math": 90
        }
    }
]
```

## Dependencies

This project currently uses only the Python standard library.

No external Python packages are required.

## Future Improvements

Possible future versions may include:

* SQLite database integration
* PostgreSQL integration
* FastAPI REST API
* Authentication and authorization
* Unit testing with pytest
* Type hints
* Dataclasses
* Custom exception classes
* Logging
* Advanced project architecture
* Web-based frontend
* Data visualization
* Cloud deployment

## Learning Outcome

This project was developed to strengthen practical Python programming skills before progressing to Advanced Python and Backend Development.

The learning progression is:

```text
Python Fundamentals
        |
        v
Object-Oriented Programming
        |
        v
File Handling and JSON
        |
        v
CRUD and Data Processing
        |
        v
Advanced Python
        |
        v
Backend Development
        |
        v
AI / Machine Learning
```

## Author

**Suparna Dey**

B.Tech CSE — Cyber Security

## License

This project is intended for educational and portfolio purposes.

