import random

class Hangman:
    """A simple Hangman game class."""
    
    def __init__(self, word_list, num_lives=5):
        """Initializes the Hangman game with given word list and number of lives."""
        self._word_list = word_list
        self._num_lives = num_lives
        self._word = random.choice(word_list)
        self._word_guessed = ['_' for _ in self._word]
        self._list_of_guesses = []

    def _is_word_guessed(self):
        """Check if the current word has been completely guessed."""
        return '_' not in self._word_guessed

    def _check_guess(self, guess):
        """Check if guessed letter is in the word and update accordingly."""
        guess = guess.lower()
        if guess in self._word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self._word):
                if letter == guess:
                    self._word_guessed[index] = guess
        else:
            self._num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self._num_lives} lives left.")

    def play(self):
        """Starts the hangman game, prompting the player for input."""
        while self._num_lives > 0 and not self._is_word_guessed():
            print("Current word status:", ' '.join(self._word_guessed))
            guess = input("Guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please enter a single alphabetical character.")
                continue
            elif guess in self._list_of_guesses:
                print("You already tried that letter!")
                continue
            else: 
                self._check_guess(guess)
                self._list_of_guesses.append(guess)
        
        if self._is_word_guessed():
            print('Congratulations. You won the game!')
        else:
            print(f'You lost! The word was {self._word}')

def main():
    word_list = ["grapefruit", "kiwi", "strawberries", "raspberries", "banana"]
    game = Hangman(word_list)
    game.play()

if __name__ == "__main__":
    main()
