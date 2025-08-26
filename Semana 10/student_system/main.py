from Ui.menu import show_menu
from Actions import (
    get_option,
    get_student_info,
    show_students,
    show_top_students,
    show_overall_average,
    remove_student,
    show_failing_students,
)
from Data import export_to_cvs, import_from_csv


def main():
    print("Welcome to the Student Control System")
    print("-" * 60)
    students = []

    while True:
        show_menu()
        option = get_option()

        if option == 1:
            while True:
                new_student = get_student_info(students)
                students.append(new_student)

                while True:
                    continue_adding = input(
                        "Do you want to add another student? (y/n): "
                    ).lower()

                    if continue_adding == "y":
                        break
                    elif continue_adding == "n":
                        break
                    else:
                        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

                if continue_adding != "y":
                    break

        elif option == 2:
            show_students(students)

        elif option == 3:
            show_top_students(students)

        elif option == 4:
            show_overall_average(students)

        elif option == 5:
            export_to_cvs(students)

        elif option == 6:
            students = import_from_csv()

        elif option == 7:
            name = input("Enter the student's name:\n").strip()
            section = input("Enter the student's section:\n").strip()
            remove_student(students, name, section)

        elif option == 8:
            show_failing_students(students)

        elif option == 9:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
