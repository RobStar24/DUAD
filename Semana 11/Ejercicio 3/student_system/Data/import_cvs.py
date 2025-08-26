import csv


class Student:
    def __init__(self, name, section, grades):
        self.name = name
        self.section = section
        self.grades = grades
        self.average = sum(grades.values()) / len(grades)


def import_from_csv(filename="students.cvs"):
    students = []

    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                grades = {
                    "Spanish": int(row["Spanish"]),
                    "English": int(row["English"]),
                    "Social Studies": int(row["Social Studies"]),
                    "Science": int(row["Science"]),
                }

                student = Student(
                    name=row["Name"], section=row["Section"], grades=grades
                )

                students.append(student)

        print(f"Data has been successfully imported from {filename}")
        return students

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
