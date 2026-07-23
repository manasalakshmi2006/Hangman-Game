# 🎮 Hangman Game in Python

A simple command-line **Hangman Game** built using Python. The game randomly selects a word, and the player must guess it one letter at a time before running out of lives.

## 📌 Features

* Random word selection
* Letter-by-letter guessing
* Tracks remaining lives
* Displays the current progress of the word
* Win and lose conditions
* Beginner-friendly Python project

## 🛠️ Technologies Used

* Python 3
* Random module (built-in)

## 📂 Project Structure

```
Hangman/
│── hangman.py
│── README.md
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/hangman-game.git
```

2. Navigate to the project folder:

```bash
cd hangman-game
```

3. Run the program:

```bash
python hangman.py
```

## 🎮 How to Play

1. The game randomly selects a word.
2. The word is displayed as underscores (`_`).
3. Enter one letter at a time.
4. If the letter is correct, it is revealed in the word.
5. If the letter is incorrect, you lose one life.
6. Guess the complete word before all lives are lost.

## 💻 Example

```
====== HANGMAN GAME ======

Word: _ _ _ _ _ _

Guess a letter: p

Word: p _ _ _ _ _

Lives Left: 6

Guess a letter: y

Word: p y _ _ _ _

Lives Left: 6

Guess a letter: z

Wrong Guess!
Lives Left: 5
```

## 📚 Concepts Used

* Variables
* Lists
* Loops
* Conditional Statements (`if-else`)
* Strings
* User Input
* Functions (optional enhancement)
* Random Module

## 🔮 Future Improvements

* Add ASCII Hangman graphics
* Prevent repeated guesses
* Add difficulty levels
* Read words from a file
* Add categories and hints
* Keep score across multiple rounds

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, improve the project, and submit a pull request.

## 📄 License

This project is open-source and available under the MIT License.

---

**Made with ❤️ using Python**
