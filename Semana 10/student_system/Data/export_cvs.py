import csv


def export_to_cvs(students, filename="students.csv"):
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
                    "Name": student["name"],
                    "Section": student["section"],
                    "Spanish": student["grades"]["Spanish"],
                    "English": student["grades"]["English"],
                    "Social Studies": student["grades"]["Social Studies"],
                    "Science": student["grades"]["Science"],
                    "Average": student["average"],
                }
                writer.writerow(student_data)

            print(f"Students data has been exported to {filename}")
