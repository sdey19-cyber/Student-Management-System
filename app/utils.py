def get_valid_integer(message, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(message))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must be at most {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_valid_marks(subject):
    return get_valid_integer(
        f"Enter marks for {subject} (0-100): ",
        0,
        100
    )


def find_student(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student

    return None


def display_student(student):
    print("\n----------------------------")
    print(f"ID         : {student.student_id}")
    print(f"Name       : {student.name}")
    print(f"Age        : {student.age}")
    print(f"Department : {student.department}")

    print("\nMarks:")

    if student.marks:
        for subject, marks in student.marks.items():
            print(f"  {subject}: {marks}")
    else:
        print("  No marks available.")

    print(f"\nTotal      : {student.get_total_marks()}")
    print(f"Average    : {student.get_average_marks():.2f}")
    print(f"Grade      : {student.get_grade()}")
    print(f"Result     : {'PASS' if student.is_pass() else 'FAIL'}")

    print("----------------------------")