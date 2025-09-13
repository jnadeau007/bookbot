"""
main.py — Entry point for the BookBot program

Usage:
    python3 main.py books/frankenstein.txt

This script:
1. Checks for a valid command-line argument (path to a .txt book).
2. Passes the file path to the generate_report() function from stats.py.
3. Exits gracefully with usage instructions if no argument is provided.
"""

from stats import *   # Import all helper functions (word/char counting, reporting)
import sys


def main():
    """
    Main entrypoint of the program.
    Validates command-line arguments and triggers the book analysis report.
    """
    if len(sys.argv) < 2:
        # If user forgot to pass a book file, print usage and exit
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Run the report on the provided book file
    generate_report(sys.argv[1])


# Only run main() when this script is executed directly
if __name__ == "__main__":
    main()
