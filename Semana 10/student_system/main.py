from Ui.menu import show_menu
from Actions import get_option, get_student_info, show_students, show_top_students, show_overall_average

def main():
    print("Welcome to the Student Control System")
    print("-" * 48)
    students = []

    while True:
        show_menu()
        option = get_option()
        
        if option == 1:
            while True:
                new_student = get_student_info()
                students.append(new_student)

                while True:
                    continue_adding = input("Do you want to add another student? (y/n): ").lower()

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


        


if __name__ == "__main__":
    main()

    