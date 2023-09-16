import random

word_list = ["Grapefruit", "Kiwi", "Strawberries", "Raspberries", "banana"]

word = random.choice(word_list)
print(word)

guess = input("Choose one letter")
if len(guess) == 1:
    print("Good guess!")
else: print("Oops! That is not a valid input.")