import sys
from random import randint
list_of_words = ["python", "java", "swift", "javascript"]
wins = 0
losses = 0


def play():
    global wins, losses
    word = list_of_words[randint(0, len(list_of_words) - 1)]
    set_of_word = set(word)
    hint = []
    guessed_letters = set()
    for i in range(len(word)):
        hint.append("-")
    attempts = 8
    while attempts > 0:
        print("")
        print("".join(hint))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("Please, input a single letter.")
        elif not letter.isalpha() or not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in guessed_letters:
            print("You've already guessed this letter.")
        else:
            guessed_letters.add(letter)
            if letter in set_of_word:
                for j in range(len(word)):
                    if word[j] == letter:
                        hint[j] = letter
                set_of_word.discard(letter)
                if len(set_of_word) == 0:
                    print(f"You guessed the word {word}!")
                    print("You survived!")
                    wins += 1
                    break
            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1
    if attempts == 0:
        print("You lost!")
        losses += 1


def results():
    print(f"You won: {wins} times.")
    print(f"You lost: {losses} times.")


def menu():
    choose = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if choose == "play":
        play()
    elif choose == "results":
        results()
    elif choose == "exit":
        sys.exit()
    menu()


print("H A N G M A N")
wins = 0
losses = 0
menu()
