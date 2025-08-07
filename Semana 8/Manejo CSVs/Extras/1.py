import csv


def print_cvs_data(path):
    with open(path) as file:
        reader = csv.DictReader(file)

        for row in reader:
            for header, value in row.items():
                print(f"{header}: {value}")
            print()


path = "Manejo CSVs/1 Video Games/videogames.csv"

print_cvs_data(path)
