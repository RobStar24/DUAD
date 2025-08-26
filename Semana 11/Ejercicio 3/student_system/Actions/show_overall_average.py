def show_overall_average(students):
    if not students:
        print("Not students registered yet")
    else:
        overall_average = sum(student['average'] for student in students) / len(students)

        print("-" * 48)
        print(f"Overall average of all students: {overall_average:.2f}")
        print("-" * 48)