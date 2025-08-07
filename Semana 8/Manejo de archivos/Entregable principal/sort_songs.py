def sort_songs(file_path):
    with open(file_path) as file:
        songs = file.readlines()
        songs.sort()
    return songs


def write_sorted_songs(file_path, output_path):
    songs = sort_songs(file_path)

    with open(output_path, "w") as output:
        for song in songs:
            output.write(song)


file_path = "Entregable principal/song_list.txt"
output_path = "Entregable principal/sorted_songs.txt"


def main():
    write_sorted_songs(file_path, output_path)


if __name__ == "__main__":
    main()
