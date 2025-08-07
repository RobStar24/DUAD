import csv


def filter_by_developer(path):
    user_input = (
        input("Enter the name of the developer you are looking for:\n").strip().lower()
    )
    with open(path) as file:
        reader = csv.DictReader(file)

        games_by_developer = []

        for row in reader:
            row_developer = row["Developer"].strip().lower()

            if row_developer.lower() == user_input:
                games_by_developer.append(row)

        if games_by_developer:
            for game in games_by_developer:
                print(
                    f"- {game['Name']} (Classification: {game['ESRB Rating'].split()[0]}, Genre: {game['Genre']})"
                )
        else:
            print(f"No games found for developer: {user_input.capitalize()}")


path = "Manejo CSVs/1 Video Games/videogames.csv"
filter_by_developer(path)
