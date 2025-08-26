import csv


def export_to_cvs(students, filename="students.cvs"):
    if not students:
        print("No students to export.")
    else:
        with open(filename, mode="w", newline="") as file:
            fieldnames = [
                "Name",
                "Section",
                "Spanish",
                "English",
                "Social Studies",
                "Science",
                "Average",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in students:
                student_data = {
                    "Name": student.name,
                    "Section": student.section,
                    "Spanish": student.grades.get("Spanish", 0),
                    "English": student.grades.get("English", 0),
                    "Social Studies": student.grades.get("Social Studies", 0),
                    "Science": student.grades.get("Science", 0),
                    "Average": student.average,
                }
                writer.writerow(student_data)

            print(f"Students data has been exported to {filename}")
