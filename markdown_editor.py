#@title programa principal
def plain():
    return input("Text:")


def bold():
    return "**{}**".format(input("Text:"))


def italic():
    return "*{}*".format(input("Text:"))


def header():
    try:
        level = int(input("Level:"))
    except ValueError:
        print("The level should be within the range of 1 to 6")
    else:
        if 1 <= level <= 6:
            return "{} {}\n".format("#" * level, input("Text:"))
        else:
            print("The level should be within the range of 1 to 6")
    return header()


def link():
    return "[{}]({})".format(input("Label:"), input("URL:"))


def inline_code():
    return "`{}`".format(input("Text:"))


def new_line():
    return "\n"


def list_(sign="*"):
    rows = int(input("Number of rows:"))
    if rows < 1:
        print("The number of rows should be greater than zero")
        return list_(sign)
    text = ""
    for i in range(rows):
        text += "{} ".format("{}.".format(i + int(sign)) if sign.isnumeric() 
                             else sign
                             )
        text += input(f"Row #{i + 1}:")
        text += "\n"
    return text


def ordered_list():
    return list_("1")


def unordered_list():
    return list_()


def help_():
    FEATURES = (
        "plain", "bold", "italic", "header", "link", "inline-code", 
        "new-line", "ordered-list", "unordered-list"
        )
    SPECIAL_COMMANDS = ("!help", "!done")
    print("Available formatters: {}".format(" ".join(FEATURES)))
    print("Special commands: {}".format(" ".join(SPECIAL_COMMANDS)))


def done(text):
    with open("output.md", "w", encoding="utf-8") as file:
        file.write("{}\n".format(text) if text[-2:] == "\n" else text)
        file.close()


def main(text_formatted):
    dict_funct = {
        "plain": plain, "bold": bold, "italic": italic, "header": header,
        "link": link, "inline-code": inline_code, "new-line": new_line,
        "unordered-list": unordered_list, "ordered-list": ordered_list,
        }
    formatter = input("Choose a formatter:")
    if formatter == "!done":
        done(text_formatted)
    elif formatter == "!help":
        help_()
    elif formatter not in dict_funct:
        print("Unknown formatting type or command")
    else:
        text_formatted += dict_funct[formatter]()
        print(text_formatted)
    if formatter != "!done":
        main(text_formatted)


if __name__ == '__main__':
    main("")
