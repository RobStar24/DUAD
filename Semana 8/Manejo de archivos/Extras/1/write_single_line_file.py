def read_file(input_path):
    with open(input_path) as file:
        lines = []
        for line in file:
            lines.append(line.strip())
    return lines


def write_file(input_path, output_path):
    lines = read_file(input_path)
    single_line_string = " ".join(lines)
    with open(output_path, "w") as output_file:
        output_file.write(single_line_string)


input_path = "Extras/1/text.txt"
output_path = "Extras/1/single_line.txt"


def main():
    write_file(input_path, output_path)


if __name__ == "__main__":
    main()
