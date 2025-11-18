def show_top_students(students):
    if len(students) < 3:
        print("Not enough students registered yet")
    else:
        top_students = sorted(
            students, key=lambda student: student.average, reverse=True
        )[:3]

        print("Top 3 students by average grade:")
        print(f"{'No.':<5} {'Name':<30} {'Section':<10} {'Average':<10}")
        print("-" * 60)

        for index, student in enumerate(top_students, start=1):
            name = student.name
            section = student.section
            average = student.average
            print(f"{index:<5} {name:<30} {section:<10} {average:<10.2f}")
