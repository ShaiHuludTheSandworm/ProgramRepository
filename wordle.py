"""
On my/our honor, Shasa Lloyd Kolar and Ethan Gomez, this 
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: SLK2633
UT EID 2: EGB664
"""

import random
import sys
import math

# ANSI escape codes for text color
# These must be used by wrapping it around a single character string
# for the test cases to work. Please use the color_word function to format
# the feedback properly.

CORRECT_COLOR = "\033[1;92m"
WRONG_SPOT_COLOR = "\033[1;93m"
NOT_IN_WORD_COLOR = "\033[1;97m"
RESET_COLOR = "\033[0m"

# If you are colorblind for yellow and green, please use these colors instead.
# Uncomment the two lines below. Commenting in and out can be done by
# highlighting the  lines you care about and using:
# on a windows/linux laptop: ctrl + /
# on a mac laptop: cmd + /

# CORRECT_COLOR = "\033[1;91m"
# WRONG_SPOT_COLOR = "\033[1;94m"

# Labels to each attempt number. Offset by 1 using "" so that the attempt
# number correctly indexes into the list so that the operation doesn't need a
# -1 every time
ATTEMPT_NUMBER = ["", "6th", "5th", "4th", "3rd", "2nd", "1st"]

# The total number of letters allowed
NUM_LETTERS = 5

INVALID_INPUT = "Bad input detected. Please try again."


def print_explanation():
    """Prints the 'how to play' instructions on the official website"""
    print("Welcome to Command Line Wordle!\n")

    print(
        "".join([NOT_IN_WORD_COLOR + letter + RESET_COLOR for letter in "How To Play"])
    )
    print("Guess the secret word in 6 tries.")
    print("Each guess must be a valid 5-letter word.")
    print("The color of the letters will change to show")
    print("how close your guess was.\n")

    print("Examples:")
    print(CORRECT_COLOR + "w" + RESET_COLOR, end="")
    print("".join([NOT_IN_WORD_COLOR + letter + RESET_COLOR for letter in "eary"]))
    print(NOT_IN_WORD_COLOR + "w" + RESET_COLOR, end=" ")
    print("is in the word and in the correct spot.")

    print(NOT_IN_WORD_COLOR + "p" + RESET_COLOR, end="")
    print(WRONG_SPOT_COLOR + "i" + RESET_COLOR, end="")
    print("".join([NOT_IN_WORD_COLOR + letter + RESET_COLOR for letter in "lls"]))
    print(NOT_IN_WORD_COLOR + "i" + RESET_COLOR, end=" ")
    print("is in the word but in the wrong spot.")

    print("".join([NOT_IN_WORD_COLOR + letter + RESET_COLOR for letter in "vague"]))
    print(NOT_IN_WORD_COLOR + "u" + RESET_COLOR, end=" ")
    print("is not in the word in any spot.\n")


def color_word(colors, word):
    """
    Colors a given word using ANSI formatting then returns it as a new string.

    pre: colors is a list of 5 strings, each representing an ANSI escape color,
         word is a string of exactly 5 characters.
    post: Returns a string where each character in word is wrapped in the
          corresponding color from colors, followed by RESET_COLOR.
    """

    assert len(colors) == 5, "List of colors must have a length of 5"
    assert len(word) == 5, "Word must have a length of 5"
    colored_word = [None] * NUM_LETTERS
    for i, character in enumerate(word):
        colored_word[i] = f"{colors[i]}{character}{RESET_COLOR}"
    return "".join(colored_word)


def prepare_game():
    """
    Prepares the game by reading in the valid words and secret words and
    then checking the command line arguments.

    If an integer is passed in, it must be converted and used as the seed for random.
    If a valid 5 letter lowercase word is passed in, it will be used as the secret word.
    All other inputs are invalid, including passing in multiple arguments in the command line.

    pre: The file valid_guesses.txt exists and contains valid guessable words, one per line.
    The file secret_words.txt exists and contains secret words, one per line.

    post: Returns a tuple which includes the secret word randomly gen or chosen, and a list of
    valid words from a txt file plus the input or throws a valueerror exception
    """

    # Specify "ascii" as its representation (encoding) since its required by pylint.

    with open("valid_guesses.txt", "r", encoding="ascii") as valid_nonsecret_words:
        valid_words = [word.rstrip() for word in valid_nonsecret_words.readlines()]

    # this file might not have to be encoded with ascii

    with open("secret_words.txt", "r", encoding="ascii") as valid_secret_words:
        possible_secret_words = [word.rstrip() for word in valid_secret_words.readlines()]

    # Checks if proper amt of arguments is provided
    # Acceptable length for sys.argv might need to be 3 based on acceptable inputs in the doc
    # Ex. python3 wordle.py 123 < 123.in or cat guesses.txt
    # python3 wordle.py (not sure if this would equate to len(sys.argv) == 3), if so...
    # (if len(sys.argv) > 3 & if len(sys.argv) == 2 or 3) would be how to solve that

    if len(sys.argv) > 2:
        raise ValueError
    #initializes arg variable
    if len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        arg = "123"

    # Checks if arg is digit, or if arg is avalid 5 char, lowercase word in list of secret words

    if arg.isdigit():
        random.seed(int(arg))
        secret_word = random.choice(possible_secret_words)
    elif len(list(arg)) == 5 and arg.islower() and arg.isalpha():
        secret_word = arg
    else:
        raise ValueError
    # might have to return None on Invalid input instead of raising a value error
    # Returns a tuple (secret_word, valid_words)

    return (secret_word, valid_words)


def is_valid_guess(guess, valid_guesses):
    """
    Checks if a given guess is valid.

    pre: guess must be a string.
         valid_guesses must be a list of strings, each string
          being a valid 5 letter lowercase guess.
    post: returns a boolean value
    """

    if guess not in valid_guesses:
        return False
    return True


def get_feedback(secret_word, guessed_word):
    """
    Processes the guess and generates the colored feedback based on the secret
    word.

    pre: secret_word must be a string of exactly 5 lowercase
         alphabetic characters.
         guessed_word must be a string of exactly 5 lowercase
         alphabetic characters.
    post: the return value is a string where:
          - Correctly guessed letters are wrapped with CORRECT_COLOR.
          - Correct letters in the wrong position are wrapped with
            WRONG_SPOT_COLOR.
          - Letters not in secret_word are wrapped with NOT_IN_WORD_COLOR.
          There will only be 5 lowercase letters with the ANSI coloring
          in the returned value.
    """

    feedback = [None] * NUM_LETTERS
    secret_letters = list(secret_word)
    guessed_letters = list(guessed_word)
    incorrect_letters = []
    # First pass of for loop for correct and not in word letters, second does wrong spot
    for i in range(NUM_LETTERS):
        if secret_letters[i] == guessed_letters[i]:
            feedback[i] = CORRECT_COLOR
        else:
            incorrect_letters.append(secret_letters[i])
            feedback[i] = NOT_IN_WORD_COLOR
    for i in range(NUM_LETTERS):
        if guessed_letters[i] in incorrect_letters and feedback[i] is not CORRECT_COLOR:
            feedback[i] = WRONG_SPOT_COLOR
            incorrect_letters.remove(guessed_letters[i])

    return color_word(feedback, guessed_word)


def main():
    """
    This function is the main loop for the game. It calls prepare_game()
    to set up the game, then it loops continuously until the game is over.
    """

    try:
        valid = prepare_game()
    except ValueError:
        print(INVALID_INPUT)
        return
    print_explanation()
    secret_word, valid_guesses = valid
    valid_guesses.append(secret_word)
    formatted_secret_word = "".join(
        [CORRECT_COLOR + c + RESET_COLOR for c in secret_word]
    )
    attempts = 6

    while attempts > 0:
        prompt = "Enter your " + ATTEMPT_NUMBER[attempts] + " guess: "
        guess = input(prompt)
        # Mimics user typing out the guess when reading input from a file.
        if not sys.stdin.isatty():
            print(guess)
        if not is_valid_guess(guess, valid_guesses):
            print(INVALID_INPUT)
            continue
        feedback = get_feedback(secret_word, guess)
        print(" " * (len(prompt) - 1), feedback)
        if feedback == formatted_secret_word:
            print("Congratulations! ", end="")
            print("You guessed the word '" + formatted_secret_word + "' correctly.")
            break
        attempts -= 1

    if attempts == 0:
        print("Sorry, you've run out of attempts. The correct word was ", end="")
        print("'" + formatted_secret_word + "'.")


if __name__ == "__main__":
    main()
