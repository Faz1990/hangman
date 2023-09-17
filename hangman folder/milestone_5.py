import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for index, letters in enumerate(self.word):
                if letters == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        

    def ask_for_input(self):
       while True:
            guess = input("Guess a letter: ")
            if not len(guess) == 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
             game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

word_list = ["grapefruit", "kiwi", "strawberries", "raspberries", "banana"]


play_game(word_list)