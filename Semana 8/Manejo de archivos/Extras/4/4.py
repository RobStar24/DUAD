def add_line(path, text):
    try:
        with open(path) as file:
            content = file.read()

            needs_newline = content and not content.endswith("\n")
    except:
        needs_newline = False

    with open(path, "a") as file:
        if needs_newline:
            file.write("\n" + text + "\n")
        else:
            file.write(text + "\n")


def main():
    user_text = input("Enter the new line of text:\n")
    path = "Extras/4/text.txt"

    try:
        add_line(path, user_text)
        print("Text added successfully")
    except Exception as ex:
        print(f"There was an error writing to file: {ex}")


if __name__ == "__main__":
    main()
