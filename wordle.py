"""
Below is a small replica of the hit game, Wordle. The intital startup of 
the code. It offeres an initial message about how to play the game if the
game is new to you. It also by default chooses a random word from the file 
of possible words. However, the code can take words from the word bank 
directly by seed or by a different files by attaching that file when
initializing the code itself. 
"""

import random
import sys

# ANSI escape codes for text color
# These must be used by wrapping it around a single character string
# for the test cases to work. Please use the color_word function to format
# the feedback properly.

CORRECT_COLOR = "\033[1;92m"
WRONG_SPOT_COLOR = "\033[1;93m"
NOT_IN_WORD_COLOR = "\033[1;97m"
RESET_COLOR = "\033[0m"

# Labels to each attempt number. Offset by 1 using "" so that the attempt number
# correctly indexes into the list so that the operation doesn't need a -1 every time
ATTEMPT_NUMBER = ["", "6th", "5th", "4th", "3rd", "2nd", "1st"]

# The total number of letters allowed
NUM_LETTERS = 5

INVALID_INPUT = "Bad input detected. Please try again."


def print_explanation():
    """Prints the 'how to play' instructions on the official website"""
    print("Welcome to Command Line Wordle!")
    print()

    print(
        "".join([NOT_IN_WORD_COLOR + letter + RESET_COLOR for letter in "How To Play"])
    )
    print("Guess the secret word in 6 tries.")
    print("Each guess must be a valid 5-letter word.")
    print("The color of the letters will change to show")
    print("how close your guess was.")
    print()

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
    print("is not in the word in any spot.")
    print()

#Below are sourced code provided by collaborators to return feedback with color just like
#in the Wordle.
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
    
    """
    #Here we start by checking the command line for what exactly is being searched for in terms or random 
    #words etc.  
    with open("valid_guesses.txt", "r", encoding = "ascii") as valid_guess_file:
        valid_words = [word.strip() for word in valid_guess_file.readlines()]

    if len(sys.argv) == 1:
        secret_word = random.choice([word.strip() for word in open("secret_words.txt", "r", encoding = "ascii")])
    elif len(sys.argv) == 2:
        term_input = sys.argv[1]
        
        if term_input.isdigit():
            random.seed(int(term_input))
            secret_word = random.choice([word.strip() for word in open("secret_words.txt","r", encoding = "ascii")])
        
        elif len(term_input) == 5 and term_input.islower():
            secret_word = term_input
       
        else:
            raise ValueError(INVALID_INPUT)
    else:
        raise ValueError(INVALID_INPUT)
    
    return secret_word, valid_words
    """
    If an integer is passed in, it must be converted and used as the seed for random.
    If a valid 5 letter lowercase word is passed in, it will be used as the secret word.
    All other inputs are invalid, including passing in multiple arguments in the command line.

    pre: The file valid_guesses.txt exists and contains valid guessable words, one per line.
         The file secret_words.txt exists and contains secret words, one per line.
    post: Returns a tuple (secret_word, valid_words) or raises a ValueError on invalid user
          secret_word: A string that is either a randomly chosen word from secret_words.txt
          or a valid 5-letter word.
          valid_words: A list of valid guess words from valid_guesses.txt.
    """


    with open("valid_guesses.txt", "r", encoding="ascii") as valid_nonsecret_words:
        valid_words = [word.rstrip() for word in valid_nonsecret_words.readlines()]


    if len(sys.argv) == 2:
        secret_word = sys.argv[1]
    else:
        secret_word = "hello"

 
    return secret_word, valid_words



def is_valid_guess(guess, valid_guesses):
    """
    Checks if a given guess is valid.

    Guess must be a string.
    valid_guesses must be a list of strings, each string
    being a valid 5 letter lowercase guess.
    post: returns a boolean value
    """

    return guess in valid_guesses and (len(guess)== NUM_LETTERS)


def get_feedback(secret_word, guessed_word):
    """
    Processes the guess and generates the colored feedback based on the secret
    word.
    """
    feedback = [NOT_IN_WORD_COLOR] * NUM_LETTERS
    secret_words = list(secret_word)


    for i in range(NUM_LETTERS):
        if guessed_word[i] == secret_word[i]:
            feedback[i] = CORRECT_COLOR
            secret_words[i] = None
    for i in range(NUM_LETTERS):
        if feedback[i] != CORRECT_COLOR and guessed_word[i] in secret_words:
            feedback[i] = WRONG_SPOT_COLOR
            # Takes out the first occurrence of the letter from secret_words
            secret_words[secret_words.index(guessed_word[i])] = None

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
