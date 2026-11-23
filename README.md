# CodeAlpha Hangman Game

## Project Description
The Hangman Game is a simple text-based word-guessing game developed using Python as part of the CodeAlpha Python Programming Internship.

The player must guess a randomly selected word one letter at a time. The player gets a maximum of 6 incorrect guesses to identify the hidden word.

## Features
- Random word selection from a predefined list of 5 words.
- Letter-by-letter guessing.
- Maximum of 6 incorrect guesses.
- Displays correctly guessed letters.
- Prevents repeated guesses.
- Validates user input.
- Displays a winning or game-over message.

## Technologies Used
- Python 3
- Random module

## Python Concepts Used
- Lists
- Loops (`while` and `for`)
- Conditional statements (`if-else`)
- Strings
- User input
- Random selection
- List operations

## How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the following command in the terminal:

```bash
python hangman.py
```

## Sample Output

```text
Welcome to Hangman Game!
Guess the word one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _ _
Enter a letter: p
Correct guess!

Word: p _ _ _ _ _
Enter a letter: x
Wrong guess!
Remaining guesses: 5
```

## Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py
└── README.md
```

## Internship
**Organization:** CodeAlpha  
**Domain:** Python Programming  
**Project:** Hangman Game

## Conclusion
This project helped me understand Python programming concepts such as loops, conditional statements, lists, strings, and random selection through a simple interactive game.
