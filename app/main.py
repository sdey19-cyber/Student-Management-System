from .student import Student
from .file_manager import load_students, save_students
from .result import subject_analysis, class_statistics
from .utils import (
    get_valid_integer,
    get_valid_marks,
    find_student,
    display_student
)


def load_student_objects():
    data = load_students()

    students = []

    for item in data:
        students.append(Student.from_dict(item))

    return students


def save_student_objects(students):
    data = []

    for student in students:
        data.append(student.to_dict())

    save_students(data)


def add_student(students):
    print("\n===== ADD STUDENT =====")

    student_id = input("Enter Student ID: ").strip()

    if find_student(students, student_id):
        print("Student ID already exists.")
        return

    name = input("Enter Name: ").strip()

    age = get_valid_integer(
        "Enter Age: ",
        1,
        100
    )

    department = input("Enter Department: ").strip()

    student = Student(
        student_id,
        name,
        age,
        department
    )

    students.append(student)

    save_student_objects(students)

    print("Student added successfully.")


def view_students(students):
    print("\n===== ALL STUDENTS =====")

    if not students:
        print("No students found.")
        return

    for student in students:
        display_student(student)


def search_student(students):
    print("\n===== SEARCH STUDENT =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if student:
        display_student(student)
    else:
        print("Student not found.")


def update_student(students):
    print("\n===== UPDATE STUDENT =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("\nLeave input blank if you don't want to change it.")

    name = input(f"Name [{student.name}]: ").strip()

    if name:
        student.name = name

    age = input(f"Age [{student.age}]: ").strip()

    if age:
        try:
            student.age = int(age)
        except ValueError:
            print("Invalid age. Keeping old age.")

    department = input(
        f"Department [{student.department}]: "
    ).strip()

    if department:
        student.department = department

    save_student_objects(students)

    print("Student updated successfully.")


def delete_student(students):
    print("\n===== DELETE STUDENT =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    confirmation = input(
        f"Delete {student.name}? (yes/no): "
    ).lower()

    if confirmation == "yes":
        students.remove(student)

        save_student_objects(students)

        print("Student deleted successfully.")
    else:
        print("Delete operation cancelled.")


def add_marks(students):
    print("\n===== ADD / UPDATE MARKS =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("\nEnter subject name.")
    subject = input("Subject: ").strip()

    marks = get_valid_marks(subject)

    student.add_marks(subject, marks)

    save_student_objects(students)

    print("Marks saved successfully.")


def remove_marks(students):
    print("\n===== REMOVE MARKS =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    subject = input("Enter Subject: ").strip()

    if subject in student.marks:
        student.remove_marks(subject)

        save_student_objects(students)

        print("Marks removed successfully.")
    else:
        print("Subject not found.")


def sort_students(students):
    print("\n===== SORT STUDENTS =====")

    if not students:
        print("No students available.")
        return

    print("""
1. Sort by Name
2. Sort by Average Marks
3. Sort by Total Marks
""")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        sorted_students = sorted(
            students,
            key=lambda student: student.name.lower()
        )

    elif choice == "2":
        sorted_students = sorted(
            students,
            key=lambda student: student.get_average_marks(),
            reverse=True
        )

    elif choice == "3":
        sorted_students = sorted(
            students,
            key=lambda student: student.get_total_marks(),
            reverse=True
        )

    else:
        print("Invalid choice.")
        return

    for student in sorted_students:
        display_student(student)


def filter_students(students):
    print("\n===== FILTER STUDENTS =====")

    print("""
1. Show PASS students
2. Show FAIL students
3. Show students with average >= 80
4. Show students with average >= 60
""")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        filtered = [
            student for student in students
            if student.is_pass()
        ]

    elif choice == "2":
        filtered = [
            student for student in students
            if not student.is_pass()
        ]

    elif choice == "3":
        filtered = [
            student for student in students
            if student.get_average_marks() >= 80
        ]

    elif choice == "4":
        filtered = [
            student for student in students
            if student.get_average_marks() >= 60
        ]

    else:
        print("Invalid choice.")
        return

    if not filtered:
        print("No matching students found.")
        return

    for student in filtered:
        display_student(student)


def main():
    students = load_student_objects()

    while True:

        print("""
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

========================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            add_marks(students)

        elif choice == "7":
            remove_marks(students)

        elif choice == "8":
            sort_students(students)

        elif choice == "9":
            filter_students(students)

        elif choice == "10":
            subject_analysis(students)

        elif choice == "11":
            class_statistics(students)

        elif choice == "12":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()