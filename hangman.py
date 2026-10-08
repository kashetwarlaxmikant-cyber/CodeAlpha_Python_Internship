import random

words = ["python", "computer", "programming", "developer", "keyboard"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=== HANGMAN GAME ===")
print("Guess the word one letter at a time.")
print("You can make up to 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess! Remaining chances:",
              max_wrong_guesses - wrong_guesses)
else:
    print("\nGame Over!")
    print("The word was:", word)
