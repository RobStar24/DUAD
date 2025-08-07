import csv


def filter_by_rating(path, valid_ratings):
    while True:
        user_input = input("Enter the ESRB rating (e.g., T, M, E):\n").upper()
        if user_input in valid_ratings:
            break
        else:
            print("Invalid rating. Please enter one of the following: M, T, E.")

    with open(path) as file:
        reader = csv.DictReader(file)

        for row in reader:
            row_rating = row["ESRB Rating"].split()[0]

            if row_rating == user_input:
                for header, value in row.items():
                    print(f"{header}: {value}")
                print()


def main():
    valid_ratings = {"E", "T", "M"}
    path = "Manejo CSVs/1 Video Games/videogames.csv"

    filter_by_rating(path, valid_ratings)


if __name__ == "__main__":
    main()
