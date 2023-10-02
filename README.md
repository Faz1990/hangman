# Classic Hangman Game

## Table of Contents
- [Description](#description)
- [Key Code Snippets](#key-code-snippets)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Enhancements/Future Work](#enhancementsfuture-work)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)
- [License](#license)

## Description
A console-based implementation of the classic Hangman game. In this project, a player is prompted to guess letters of a randomly selected word from a predefined list. The goal of this project was to hone Python programming skills, particularly emphasizing object-oriented programming and user interaction.

**What it does**:  
The game prompts the user for letter inputs and displays the current status of the guessed word, replacing underscores with correctly guessed letters. The game ends when the player either correctly guesses the entire word or runs out of lives.

**Aim of the project**:  
To create a fun, interactive game that also serves as a demonstration of Python's capabilities in terms of logic and user interaction.

**What I learned**:
- Object-Oriented Programming in Python
- Handling user input and validation
- String manipulation and control structures

## Key Code Snippets


#### 1. Checking User Guess
This piece of code checks whether the user's guessed letter is in the word or not. Handling correct and incorrect guesses was a crucial part of the game logic.

def _check_guess(self, guess):

#... (rest of the code)

#### 2. User Input Validation

Ensuring the user's input was both valid and hadn't been previously guessed was a challenge. This block handles both of those checks:


guess = input("Guess a letter: ")

#... (rest of the code)


#### 3. Game Loop
Keeping the game running while the word hasn't been guessed entirely or lives remain was vital. Here's how the main game loop was structured:

while self._num_lives > 0 and not self._is_word_guessed():

#... (rest of the code)



## Installation
Ensure you have Python 3.x installed on your machine.

Clone the repository:

git clone https://github.com/Faz1990/hangman.git

Navigate to the project directory:

cd hangman

## Usage
In the terminal, run the game using:

python hangman.py

Follow the on-screen prompts to play the game.

## File Structure

hangman/

│

├── hangman.py   # The main game file containing all logic and classes.

│

└── README.md    # This file, explaining the project and its use.

## Enhancements/Future Work

Add support for multiple difficulty levels.
Include a larger dictionary or integrate with an API for word fetching.
Offer hints to the user.

## Acknowledgments

AiCore for their guidance.

## Contact
For any feedback or collaboration opportunities, reach out to me at faisal1990@hotmai.co.uk.

## License
This project is under the MIT License. See the LICENSE file for more details.
