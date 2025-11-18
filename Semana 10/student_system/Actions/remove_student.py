def remove_student(students, name, section):
    student_to_remove = None

    for student in students:
        if (
            student["name"].lower() == name.lower()
            and student["section"] == section.upper()
        ):
            student_to_remove = student
            break

    if student_to_remove:
        confirm = input(
            f"Are you sure you want to remove {name} from section {section}? (y/n): "
        ).lower()
        if confirm == "y":
            students.remove(student_to_remove)
            print(f"Student {name} from section {section} has been removed.")
        else:
            print("Student removal cancelled.")

    else:
        print(f"No student found with name {name} and section {section}.")
