<<<<<<< HEAD
from collections import Counter

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = count_words("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(" ")
    count_character("books/frankenstein.txt")
    print("--- End report ---")

def count_words(book):
    # get the file contents from book
    with open(book) as f:
        file_contents = f.read()
        #get the word count from file_contents
        word_count = len(file_contents.split())
        #loop throught the file_contents and add 1 for each char
    return word_count # return the word_count output

def sort_on(dict):
    return dict['count']

def count_character(book):
    report_lines = []
    with open(book) as f:
        file_contents = f.read()
        words_lower_case = file_contents.lower()
        character_count_dictionary = Counter(words_lower_case)
        for key, value in character_count_dictionary.items():
            if key.isalpha():
               report_lines.append({"character": key, "count":value}) 

        report_lines.sort(reverse=True, key=sort_on)
        for sentence in report_lines:
            print(f"The '{sentence['character']}' character was found {sentence['count']} times")

if __name__ == '__main__':
    main()
=======
from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    generate_report(sys.argv[1])


main()
>>>>>>> b62c7e6 (added statistics functionality and report generate function to render various data points for a book that a user runs this program on)
