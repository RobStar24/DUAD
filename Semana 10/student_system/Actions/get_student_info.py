import re


def get_valid_grade(subject):
    while True:
        try:
            grade = int(input(f"Enter {subject} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                raise ValueError
        except ValueError:
            print("Error: Select a valid grade (0-100)")


def get_valid_name():
    while True:
        name = input("Enter student's full name: ")
        if len(name) > 2 and all(char.isalpha() or char.isspace() for char in name):
            return name
        else:
            print("Error: Please enter a valid name.")


def validate_section(section):
    pattern = r"^\d{1,2}[A-Z]$"
    return bool(re.match(pattern, section))


def get_valid_section():
    while True:
        section = input("Enter section (e.g., 9C, 10A): ").upper()
        if validate_section(section):
            return section
        else:
            print("Invalid format. Please enter a valid section like '9C' or '10A'.")


def calculate_average(grades):
    return sum(grades.values()) / len(grades)



def get_student_info():
    name = get_valid_name()
    section = get_valid_section()

    subjects = ["Spanish", "English", "Social Studies", "Science"]

    grades = {}

    for subject in subjects:
        grades[subject] = get_valid_grade(subject)

    average = calculate_average(grades)

    return {
        'name': name,
        'section': section,
        'grades': grades,
        'average': average
    }
