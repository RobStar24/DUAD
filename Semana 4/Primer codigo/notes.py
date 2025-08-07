def notes():
    notes_amount = 0
    notes_counter = 1
    current_note = 0
    approved_notes = 0
    failed_notes = 0
    approved_notes_average = 0
    failed_notes_average = 0
    total_average = 0

    notes_amount = int(input("How many grades are there in total \n"))

    while (notes_counter <= notes_amount):
        current_note = int(
            input(f"Enter the grade number: {notes_counter} \n"))

        if (current_note < 70):
            failed_notes += 1
            failed_notes_average += current_note

        else:
            approved_notes += 1
            approved_notes_average += current_note

        total_average += current_note
        notes_counter += 1

    total_average = total_average / notes_amount

    if (approved_notes > 0):
        approved_notes_average = approved_notes_average / approved_notes
    else:
        approved_notes_average = 0

    if (failed_notes > 0):
        failed_notes_average = failed_notes_average / failed_notes
    else:
        failed_notes_average = 0

    print(f"The student passed this number of grades: {approved_notes}")
    print(f"This is the average of approved grades: {approved_notes_average}")
    print(f"The student failed this number of grades: {failed_notes}")
    print(f"This is the average of failed grades: {failed_notes_average}")
    print(f"This is the Total Average: {total_average}")


notes()
