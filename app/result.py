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
        student
        for student in students
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