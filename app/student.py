class Student:
    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def update_marks(self, subject, marks):
        if subject in self.marks:
            self.marks[subject] = marks
        else:
            print(f"{subject} marks not found.")

    def remove_marks(self, subject):
        if subject in self.marks:
            del self.marks[subject]
        else:
            print(f"{subject} marks not found.")

    def get_total_marks(self):
        return sum(self.marks.values())

    def get_average_marks(self):
        if not self.marks:
            return 0

        return self.get_total_marks() / len(self.marks)

    def get_grade(self):
        average = self.get_average_marks()

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

    def is_pass(self):
        if not self.marks:
            return False

        return all(mark >= 40 for mark in self.marks.values())

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["department"]
        )

        student.marks = data.get("marks", {})

        return student