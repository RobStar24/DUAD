import csv


def import_from_csv(filename="students.cvs"):
    students = []

    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "name": row["Name"],
                    "section": row["Section"],
                    "grades": {
                        "Spanish": int(row["Spanish"]),
                        "English": int(row["English"]),
                        "Social Studies": int(row["Social Studies"]),
                        "Science": int(row["Science"]),
                    },
                    "average": float(row["Average"]),
                }
                students.append(student)

        print(f"Data has been successfully imported from {filename}")
        return students

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
