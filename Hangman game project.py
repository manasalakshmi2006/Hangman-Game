import random

words = [
    "python",
    "computer",
    "program",
    "developer",
    "keyboard",
    "internet",
    "science",
    "machine",
    "network",
    "project"
]

chosen_word = random.choice(words)

display = []

for letter in chosen_word:
    display.append("_")

lives = 6

print("====== HANGMAN GAME ======")

while lives > 0 and "_" in display:

    print("\nWord:", " ".join(display))

    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:

        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

    else:
        lives -= 1
        print("Wrong Guess!")

    print("Lives Left:", lives)

if "_" not in display:
    print("\nCongratulations! You Won!")
    print("Word:", chosen_word)
else:
    print("\nGame Over!")
    print("The word was:", chosen_word)