def parse_upper(path):
    upper_words = []
    with open(path) as file:
        for line in file:
            upper_words.append(line.upper())

    return upper_words


def write_file(path, output_path):
    upper_words = parse_upper(path)
    with open(output_path, "w") as output:
        for line in upper_words:
            output.write(line)


input_path = "Extras/3/text.txt"
output_path = "Extras/3/upper_text.txt"


def main():
    write_file(input_path, output_path)


if __name__ == "__main__":
    main()
