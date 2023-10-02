import random

word_list = ["grapefruit", "kiwi", "strawberries", "raspberries", "banana"]

word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else: print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

ask_for_input()