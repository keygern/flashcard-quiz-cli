# 🧠 Flashcard Quiz CLI App

A simple command-line flashcard quiz application written in Python.  
It allows you to test your knowledge using custom flashcards stored in a `.json` file — and even add your own questions to grow the quiz.

---

## ✨ Features

- Randomized quiz question order each session
- Create new flashcards via command-line input
- JSON-based storage for persistence
- Modular code structure with separation of logic
- Unit tested using `pytest`

---

## 🚀 How to Run

Make sure you have Python 3.10+ installed.

1. Clone this repo:
   ```bash
   git clone https://github.com/keygern/flashcard-quiz-cli.git
   cd flashcard-quiz-cli
2. Run the App
    python main.py
3. Follow prompts to start the quiz and add flashcards at the end if desired

## 🧪 How to Test
1. Install pytest
    pip install pytest
2. Run tests
    pytest

## 📁 File Structure
flashcard_app/
├── main.py              # Runs the app
├── flashcard.py         # Flashcard class definition
├── utils.py             # JSON load/save helpers
├── flashcards.json      # Flashcard data
├── test_flashcard.py    # Pytest test file
└── README.md            # This file

## 🧰 Stack

Python 3.10+
json for data storage
random for shuffling questions
pytest for unit testing

-> Pull requests, forks, and suggestions welcome!

