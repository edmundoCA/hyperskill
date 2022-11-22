from random import randint
from random import choice


def addition(a, b, *args):
    return a + b


def subtraction(a, b, *args):
    return a - b


def multiplication(a, b, *args):
    return a * b


def user_guess():
    prompt = input()
    try:
        return int(prompt)
    except ValueError:
        print("Incorrect format.")
    return user_guess()


def user_level():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    prompt = input()
    if prompt not in ("1", "2"):
        print("Incorrect format.")
        return user_level()
    return int(prompt)


def appending_text_to_file(text):
    with open("results.txt", "a", encoding='utf-8') as file:
        file.write(text)


def main():
    operators = {"+": addition, "-": subtraction, "*": multiplication}
    operators_tuple = ("+", "-", "*")
    right_answers = 0

    level = user_level()

    for _ in range(5):
        if level == 1:
            expression = (randint(2, 9), choice(operators_tuple), randint(2, 9))
            print(*expression)
            res = operators[expression[1]](expression[0], expression[2])
        else:
            square = randint(11, 29)
            print(square)
            res = square ** 2
        answer = user_guess()
        if res == answer:
            print("Right!")
            right_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {right_answers}/5")

    print("Would you like to save the result? Enter yes or no.")
    save_the_result = input()
    if save_the_result in ("yes", "YES", "y", "Yes"):
        print("What is your name?")
        name = input()
        text = "{}: {}/5 in level {} ({})".format(
            name, right_answers, level,
            "simple operations with numbers 2-9" if level == 1 else "integral squares 11-29"
        )
        appending_text_to_file(text)
        print('The results are saved in "results.txt".')


if __name__ == "__main__":
    main()
