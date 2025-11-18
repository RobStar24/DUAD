def show_students(students):
    if not students:
        print("No students registered yet.")
    else:
        print(f"{'No.':<5} {'Name':<30} {'Section':<10} {'Spanish':<8}| {'English':<8}| {'Social Studies':<15}| {'Science':<8}| {'Average':<8}")
        print("-" * 110)

        for index, student in enumerate(students, start=1):
            name = student['name']
            section = student['section']
            grades = student['grades']
            average = student['average'] 

            print(f"{index:<5} {name:<30} {section:<10} {grades['Spanish']:<8} {grades['English']:<8} {grades['Social Studies']:<15} {grades['Science']:<8} {average:<8.2f}")