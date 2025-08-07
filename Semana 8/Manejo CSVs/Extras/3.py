import csv


def get_games_genres(path):
    with open(path) as file:
        reader = csv.DictReader(file)
        genres_count = {}

        for row in reader:
            row_genre = row["Genre"]
            if row_genre not in genres_count:
                genres_count[row_genre] = 1
            else:
                genres_count[row_genre] += 1

        print("Genres found:")
        for genre, count in genres_count.items():
            print(f"{genre}: {count}")
        print()


path = "Manejo CSVs/1 Video Games/videogames.csv"

get_games_genres(path)
