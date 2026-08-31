# Python-Based Student Management System

import json
import numpy as np
import pandas as pd

students = []
FILE_NAME = "students.json"

def get_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Value must not be greater than {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_marks(prompt):
    while True:
        try:
            marks = float(input(prompt))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_student():
    print("\n========== ADD STUDENT ==========")

    student_id = get_integer(
        "Enter Student ID: ",
        min_value=1
    )

    for student in students:
        if student["id"] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter Student Name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter Student Name: ").strip()

    age = get_integer(
        "Enter Student Age: ",
        min_value=1,
        max_value=100
    )

    course = input("Enter Course: ").strip()

    while not course:
        print("Course cannot be empty.")
        course = input("Enter Course: ").strip()

    year = get_integer(
        "Enter Year: ",
        min_value=1,
        max_value=4
    )

    marks = get_marks("Enter Marks: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "year": year,
        "marks": marks
    }

    students.append(student)
    save_students()

    print("\nStudent added successfully!")

def view_students():
    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("\nStudent ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("Year       :", student["year"])
        print("Marks      :", student["marks"])
        print("----------------------------------")


def search_student():
    print("\n========== SEARCH STUDENT ==========")

    student_id = get_integer(
    "Enter Student ID to search: ",
    min_value=1
)

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("----------------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Year       :", student["year"])
            print("Marks      :", student["marks"])
            print("----------------------------------")
            return

    print("\nStudent not found.")



def update_student():
    print("\n========== UPDATE STUDENT ==========")

    student_id = get_integer(
        "Enter Student ID to update: ",
        min_value=1
    )

    for student in students:
        if student["id"] == student_id:

            print("\nStudent Found!")
            print("----------------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Year       :", student["year"])
            print("Marks      :", student["marks"])
            print("----------------------------------")

            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            print("4. Year")
            print("5. Marks")
            print("6. Update All")
            print("7. Cancel")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter new Student Name: ").strip()

                while not name:
                    print("Name cannot be empty.")
                    name = input("Enter new Student Name: ").strip()

                student["name"] = name

            elif choice == "2":
                student["age"] = get_integer(
                    "Enter new Student Age: ",
                    min_value=1,
                    max_value=100
                )

            elif choice == "3":
                course = input("Enter new Course: ").strip()

                while not course:
                    print("Course cannot be empty.")
                    course = input("Enter new Course: ").strip()

                student["course"] = course

            elif choice == "4":
                student["year"] = get_integer(
                    "Enter new Year: ",
                    min_value=1,
                    max_value=4
                )

            elif choice == "5":
                student["marks"] = get_marks(
                    "Enter new Marks: "
                )

            elif choice == "6":
                name = input("Enter new Student Name: ").strip()

                while not name:
                    print("Name cannot be empty.")
                    name = input("Enter new Student Name: ").strip()

                age = get_integer(
                    "Enter new Student Age: ",
                    min_value=1,
                    max_value=100
                )

                course = input("Enter new Course: ").strip()

                while not course:
                    print("Course cannot be empty.")
                    course = input("Enter new Course: ").strip()

                year = get_integer(
                    "Enter new Year: ",
                    min_value=1,
                    max_value=4
                )

                marks = get_marks(
                    "Enter new Marks: "
                )

                student["name"] = name
                student["age"] = age
                student["course"] = course
                student["year"] = year
                student["marks"] = marks

            elif choice == "7":
                print("\nUpdate cancelled.")
                return

            else:
                print("\nInvalid choice.")
                return

            save_students()
            print("\nStudent record updated successfully!")
            return

    print("\nStudent not found.")



def delete_student():
    print("\n========== DELETE STUDENT ==========")

    student_id = get_integer(
    "Enter Student ID to delete: ",
    min_value=1
)

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students()

            print("\nStudent record deleted successfully!")
            return

    print("\nStudent not found.")


def calculate_grade():
    print("\n========== CALCULATE GRADE ==========")

    student_id = get_integer(
    "Enter Student ID: ",
    min_value=1
)

    for student in students:
        if student["id"] == student_id:
            marks = student["marks"]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\nStudent Name :", student["name"])
            print("Marks        :", marks)
            print("Grade        :", grade)
            return

    print("\nStudent not found.")


def performance_analysis():
    print("\n========== PERFORMANCE ANALYSIS ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    df = pd.DataFrame(students)

    marks = np.array(df["marks"])

    print("\nStudent Performance Table:")
    print(df[["id", "name", "course", "marks"]].to_string(index=False))

    print("\n========== STATISTICS ==========")
    print("Total Students       :", len(df))
    print("Average Marks        :", round(np.mean(marks), 2))
    print("Median Marks         :", round(np.median(marks), 2))
    print("Highest Marks        :", np.max(marks))
    print("Lowest Marks         :", np.min(marks))
    print("Standard Deviation   :", round(np.std(marks), 2))

    passed = len(df[df["marks"] >= 50])
    failed = len(df[df["marks"] < 50])

    print("Passed Students      :", passed)
    print("Failed Students      :", failed)

    print("\nStudents Sorted by Marks:")
    sorted_df = df.sort_values(by="marks", ascending=False)
    print(sorted_df[["id", "name", "marks"]].to_string(index=False))



def load_students():
    global students

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    except json.JSONDecodeError:
        print("Warning: Student data file is invalid.")
        students = []


def save_students():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Error: Unable to save student records.")



def main():
    load_students()
    while True:
        print("\n========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Grade")
        print("7. Performance Analysis")
        print("8. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            calculate_grade()

        elif choice == "7":
            performance_analysis()

        elif choice == "8":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
