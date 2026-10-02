import json

FILE_NAME = "data/students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: students.json contains invalid JSON.")
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

    print("Student data saved successfully.")