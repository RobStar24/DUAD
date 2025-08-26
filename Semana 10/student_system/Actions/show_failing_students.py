def show_failing_students(students):
    failing_students = []

    for student in students:
        failed_subjects = []
        for subject, grade in student["grades"].items():
            if grade < 60:
                failed_subjects.append((subject, grade))

        if failed_subjects:
            failing_students.append(
                {
                    "name": student["name"],
                    "section": student["section"],
                    "failed_subjects": failed_subjects,
                }
            )

    if failing_students:
        print(f"\n{'Name':<20} {'Section':<10} {'Failed Subjects':<40}")
        print("-" * 80)
        for student in failing_students:
            failed_str = ", ".join(
                [
                    f"{subject} ({grade})"
                    for subject, grade in student["failed_subjects"]
                ]
            )
            print(f"{student['name']:<20} {student['section']:<10} {failed_str:<40}")
    else:
        print("No students are failing any subjects.")
