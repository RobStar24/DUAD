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
        if len(name) > 2 and all(char.isalpha() or char.isspace() for char in name)
            return name
        else:
            print("Error: Please enter a valid name.")


def get_student_info():
    name = get_valid_name()
    section = input("Enter section: ")

    subjects = ["Spanish", "English", "Social Studies", "Science"]

    grades = {}

    for subject in subjects:
        grades[subject] = get_valid_grade(subject)

    return {
        'name': name,
        'section': section,
        'grades': grades
    }

