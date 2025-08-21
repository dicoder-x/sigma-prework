""""""
import random


def check(string: str, guess: str) -> str:
    """Checks two strings against each other"""
    result = ['_' for _ in range(len(string))]
    for i, char in enumerate(guess):
        if char == string[i]:
            result[i] = char
        elif char in string:
            result[i] = '?'
    return result


def generate_word(word_list: list) -> str:
    """Randomly selects a word from a list of words"""
    return random.choice(word_list)


def guess_game(word_list: list):
    """Guessing the 5-letter word game within 5 turns"""
    answer = generate_word(word_list)
    turns = 5
    while turns > 0:
        guess = input("Enter your guess: ")
        if len(answer) != 5:
            print("Please enter a 5-letter word.")
            continue
        result = check(answer, guess)
        print(' '.join(result))
        if guess == answer:
            print("Congratulations! You've guessed the word.")
            return
        turns -= 1
    print(f"Sorry, you didn't guess the word. The word was {answer}.")


list2 = ["apple", "place", "grape", "chair", "spear", "green",
         "plant", "house", "water", "money", "tiger", "panda"]

guess_game(list2)
