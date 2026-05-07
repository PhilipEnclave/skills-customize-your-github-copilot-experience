
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Students will practice string manipulation, conditionals, and random selection by creating a fully playable Hangman game.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the core game structure that randomly selects a word and tracks the player's progress throughout the game.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list using the `random` module
- Display the hidden word as underscores (e.g., `_ _ _ _ _`) at the start
- Track which letters have already been guessed
- Keep count of incorrect guesses remaining (start with 6 attempts)

### 🛠️ Implement the Game Loop

#### Description
Add the interactive loop that accepts player input, validates guesses, and updates the game state until the game ends.

#### Requirements
Completed program should:

- Prompt the player to enter a letter guess each turn
- Reveal correctly guessed letters in their proper positions
- Decrement remaining attempts for each incorrect guess
- Display the updated word progress and remaining attempts after each guess
- End the game when the word is fully guessed or attempts are exhausted
- Display a win message if the word is guessed, or a loss message (revealing the word) if attempts run out
