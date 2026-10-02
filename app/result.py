def calculate_total(marks):
    return sum(marks.values())


def calculate_average(marks):
    if not marks:
        return 0

    return calculate_total(marks) / len(marks)


def calculate_grade(marks):
    average = calculate_average(marks)

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def check_pass_fail(marks):
    if not marks:
        return "No marks"

    if all(mark >= 40 for mark in marks.values()):
        return "PASS"

    return "FAIL"


def subject_analysis(students):
    if not students:
        print("No students available.")
        return

    subjects = set()

    for student in students:
        subjects.update(student.marks.keys())

    print("\n===== SUBJECT-WISE ANALYSIS =====")

    for subject in sorted(subjects):
        marks = []

        for student in students:
            if subject in student.marks:
                marks.append(student.marks[subject])

        if marks:
            average = sum(marks) / len(marks)

            print(f"\nSubject: {subject}")
            print(f"Average: {average:.2f}")
            print(f"Highest: {max(marks)}")
            print(f"Lowest: {min(marks)}")


def class_statistics(students):
    if not students:
        print("No students available.")
        return

    students_with_marks = [
        student for student in students
        if student.marks
    ]

    if not students_with_marks:
        print("No marks available.")
        return

    topper = max(
        students_with_marks,
        key=lambda student: student.get_average_marks()
    )

    class_average = sum(
        student.get_average_marks()
        for student in students_with_marks
    ) / len(students_with_marks)

    print("\n===== CLASS STATISTICS =====")

    print(f"Class Average: {class_average:.2f}")

    print(
        f"Topper: {topper.name} "
        f"({topper.get_average_marks():.2f})"
    )

    print(f"Topper Grade: {topper.get_grade()}")