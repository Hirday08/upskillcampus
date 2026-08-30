# Python-Based Student Management System

A console-based Student Management System developed in Python as part of a four-week Python Learning Internship through **Upskill Campus**, **The IoT Academy**, and **UniConverge Technologies Pvt. Ltd. (UCT)**.

## Project Overview

The Student Management System is designed to manage student records through a simple menu-driven console application.

The system allows users to add, view, search, update, and delete student records. It also provides grade calculation and student performance analysis using **NumPy** and **Pandas**.

Student information is stored in a JSON file, allowing records to remain available when the application is restarted.

## Features

* Add new student records
* View all student records
* Search students using Student ID
* Update individual student fields
* Update all student details
* Delete student records
* Calculate student grades based on marks
* Perform student performance analysis
* Calculate average and median marks
* Find highest and lowest marks
* Calculate standard deviation
* Display passed and failed students
* Sort students according to marks
* Validate user input
* Handle invalid numerical input
* Store data permanently using JSON

## Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **JSON**
* **Git**
* **GitHub**

## Python Concepts Used

The project demonstrates the following Python concepts:

* Variables and data types
* Conditional statements (`if`, `elif`, `else`)
* Loops
* Functions
* Lists
* Dictionaries
* Exception handling
* File handling
* JSON data storage
* Input validation
* Modular programming

## NumPy and Pandas

### Pandas

Pandas is used to convert student records into a DataFrame and perform operations such as:

* Displaying student data in tabular form
* Filtering student records
* Sorting students by marks
* Counting passed and failed students

### NumPy

NumPy is used for numerical analysis of student marks, including:

* Mean
* Median
* Minimum
* Maximum
* Standard deviation

## Project Structure

```text
upskillcampus/
│
├── StudentManagementSystem.py
├── students.json
├── requirements.txt
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Hirday08/upskillcampus
```

### 2. Open the project folder

```bash
cd upskillcampus
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python StudentManagementSystem.py
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
6. Calculate Grade
7. Performance Analysis
8. Exit
========================================
```

## Data Storage

Student records are stored in `students.json` using JSON format.

The application loads the saved records when it starts and updates the file whenever a student is added, updated, or deleted.

## Performance Analysis

The Performance Analysis module uses NumPy and Pandas to analyze student marks and provide useful statistics.

The analysis includes:

* Total number of students
* Average marks
* Median marks
* Highest marks
* Lowest marks
* Standard deviation
* Number of passed students
* Number of failed students
* Students sorted by marks

## Future Improvements

Possible future improvements include:

* Graphical User Interface (GUI)
* Database integration using MySQL or SQLite
* Student attendance management
* Subject-wise marks
* Exporting reports to Excel or PDF
* User authentication
* Advanced performance charts

## Internship

This project was developed as part of a **four-week Python Learning Internship** through:

* Upskill Campus
* The IoT Academy
* UniConverge Technologies Pvt. Ltd. (UCT)

The internship provided practical exposure to Python programming, problem-solving, file handling, data analysis, and basic software development practices.