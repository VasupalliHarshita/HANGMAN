# Hangman Game (Python)

## Project Overview

Hangman is a simple text-based word guessing game developed in Python. The computer randomly selects a word from a predefined list, and the player attempts to guess the word one letter at a time. The player has a maximum of **6 incorrect guesses** before the game ends.

This project is designed for beginners to practice fundamental Python programming concepts such as loops, conditional statements, lists, strings, functions, and the `random` module.

---

## Features

* Randomly selects a word from a predefined list of five words.
* Displays the hidden word using underscores (`_`).
* Accepts one letter as input from the player.
* Reveals all matching letters when the guess is correct.
* Allows a maximum of **6 incorrect guesses**.
* Prevents duplicate letter guesses.
* Displays remaining attempts after each guess.
* Announces whether the player has won or lost.
* Console-based application with no external libraries required.

---

## Technologies Used

* Python 3
* Built-in `random` module

---

## Python Concepts Used

* Variables
* Lists
* Strings
* `while` loop
* `for` loop
* `if-else` statements
* User Input (`input()`)
* String methods (`lower()`, `isalpha()`)
* Random module (`random.choice()`)

---

## Project Structure

```text
Hangman/
│
├── hangman.py      # Main Python program
└── README.md       # Project documentation
```

---

## How the Game Works

1. The program starts by importing the `random` module.
2. A list of five predefined words is created.
3. The computer randomly selects one word.
4. The selected word is hidden using underscores.
5. The player has **6 incorrect attempts**.
6. The player enters one letter at a time.
7. If the guessed letter exists in the word:

   * All occurrences of the letter are revealed.
8. If the guessed letter is incorrect:

   * The remaining attempts decrease by one.
9. The game continues until:

   * The player guesses the complete word, or
   * The player runs out of attempts.
10. The final result (Win/Lose) is displayed.

---

## Algorithm

1. Import the `random` module.
2. Create a list of predefined words.
3. Randomly select a secret word.
4. Create a hidden version of the word using underscores.
5. Initialize the number of attempts to **6**.
6. Create an empty list to store guessed letters.
7. Repeat while attempts remain and the word is not completely guessed:

   * Display the current hidden word.
   * Ask the player to enter a letter.
   * Validate the input.
   * Check whether the letter has already been guessed.
   * If the letter is present in the secret word:

     * Reveal all matching letters.
   * Otherwise:

     * Decrease the remaining attempts.
8. If all letters are guessed, display a winning message.
9. Otherwise, display a game-over message and reveal the secret word.

---

## Sample Output

```text
WELCOME TO HANGMAN GAME

Current Word: _ _ _ _ _
Remaining Attempts: 6

Enter a letter: r

Correct Guess!

Current Word: r _ _ _ _
Remaining Attempts: 6

Enter a letter: o

Correct Guess!

Current Word: r o _ o _
Remaining Attempts: 6
```

### Winning Output

```text
Congratulations!
You guessed the word: ROBOT
```

### Losing Output

```text
Game Over!
The correct word was: TIGER
```

---

## Time Complexity

* **Time Complexity:** O(n) per guess, where **n** is the length of the secret word.
* **Space Complexity:** O(n) for storing the hidden word.

---

## Learning Outcomes

After completing this project, you will understand how to:

* Work with lists and strings.
* Use the `random` module.
* Implement loops and conditional statements.
* Validate user input.
* Track game progress using variables.
* Build an interactive console application.

---

## Future Enhancements

* Add difficulty levels (Easy, Medium, Hard).
* Read words from an external file.
* Display ASCII art for the hangman after each incorrect guess.
* Allow multiple rounds without restarting the program.
* Add categories such as Animals, Fruits, Countries, and Movies.
* Maintain a score and high-score system.
* Provide hints for difficult words.

---

## Author

**Harshita Vasupalli**

Engineering Student

GitHub: https://github.com/VasupalliHarshita
