# 📚 BookBot

BookBot is a Python program that analyzes books and generates a detailed report of their contents.  
It counts words, tracks character frequencies, and organizes the results into a clean, human-readable report.

---

## 🚀 Features
- 📖 **Word Count**: Counts the total number of words in the book.
- 🔠 **Character Frequency**: Counts how often each letter appears, ignoring case.
- 📊 **Sorted Report**: Displays results sorted from most common to least common letters.
- ⚡ **Command Line Tool**: Run it on any `.txt` file with a single command.

---

## 🛠️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bookbot.git
   cd bookbot

2. Make sure you have Python 3.9+ installed
    run: python3 --version

3. Add your .txt books into the books/ directory

▶️ Usage
- Run BookBot from the command line and pass in the path to the book:
    python3 main.py books/[NAMEOFBOOK.txt]

📊 Example Output
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
...
============= END ===============

