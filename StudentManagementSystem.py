# Python-Based Student Management System

students = []

def add_student():
    print("\n========== ADD STUDENT ==========")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")
    year = int(input("Enter Year: "))
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "year": year,
        "marks": marks
    }

    students.append(student)

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

    student_id = int(input("Enter Student ID to search: "))

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

    student_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Enter new details:")

            student["name"] = input("Enter Student Name: ")
            student["age"] = int(input("Enter Student Age: "))
            student["course"] = input("Enter Course: ")
            student["year"] = int(input("Enter Year: "))
            student["marks"] = float(input("Enter Marks: "))

            print("\nStudent record updated successfully!")
            return

    print("\nStudent not found.")



def delete_student():
    print("\n========== DELETE STUDENT ==========")

    student_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("\nStudent record deleted successfully!")
            return

    print("\nStudent not found.")



def main():
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
        print("7. Exit")
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
            print("\nCalculate Grade selected.")

        elif choice == "7":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()