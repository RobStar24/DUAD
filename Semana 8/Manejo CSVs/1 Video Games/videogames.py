import csv

video_games = [
    {
        "Name": "The Last of Us Part II",
        "Genre": "Action-Adventure",
        "Developer": "Naughty Dog",
        "ESRB Rating": "M (Mature)",
    },
    {
        "Name": "Cyberpunk 2077",
        "Genre": "RPG (Role-Playing Game)",
        "Developer": "CD Projekt Red",
        "ESRB Rating": "M (Mature)",
    },
    {
        "Name": "Super Mario Odyssey",
        "Genre": "Platformer",
        "Developer": "Nintendo",
        "ESRB Rating": "E (Everyone)",
    },
    {
        "Name": "Red Dead Redemption 2",
        "Genre": "Action-Adventure",
        "Developer": "Rockstar Games",
        "ESRB Rating": "M (Mature)",
    },
    {
        "Name": "Minecraft",
        "Genre": "Sandbox",
        "Developer": "Mojang Studios",
        "ESRB Rating": "E (Everyone)",
    },
    {
        "Name": "The Witcher 3: Wild Hunt",
        "Genre": "RPG (Role-Playing Game)",
        "Developer": "CD Projekt Red",
        "ESRB Rating": "M (Mature)",
    },
    {
        "Name": "Fortnite",
        "Genre": "Battle Royale",
        "Developer": "Epic Games",
        "ESRB Rating": "T (Teen)",
    },
    {
        "Name": "Animal Crossing: New Horizons",
        "Genre": "Social Simulation",
        "Developer": "Nintendo",
        "ESRB Rating": "E (Everyone)",
    },
    {
        "Name": "Overwatch",
        "Genre": "First-Person Shooter",
        "Developer": "Blizzard Entertainment",
        "ESRB Rating": "T (Teen)",
    },
    {
        "Name": "Hades",
        "Genre": "Action Roguelike",
        "Developer": "Supergiant Games",
        "ESRB Rating": "M (Mature)",
    },
]


def write_csv_file(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


write_csv_file(
    "Manejo CSVs/1 Video Games/videogames.csv", video_games, video_games[0].keys()
)
