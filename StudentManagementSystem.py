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
            print("\nView All Students selected.")

        elif choice == "3":
            print("\nSearch Student selected.")

        elif choice == "4":
            print("\nUpdate Student selected.")

        elif choice == "5":
            print("\nDelete Student selected.")

        elif choice == "6":
            print("\nCalculate Grade selected.")

        elif choice == "7":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()