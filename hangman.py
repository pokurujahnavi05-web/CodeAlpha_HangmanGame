import random

# List of 5 predefined words
words = ["python", "apple", " mango", "school", "computer"]

# Select a random word
secret_word = random.choice(words).strip()

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_guesses:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        break

    # Get input from player
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining guesses:", max_guesses - wrong_guesses)

# Game over
if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The word was:", secret_word)