def get_num_words(pathToFile):
    """
    Reads a book file and returns the total number of words.
    """
    book = get_book_text(pathToFile)      # Get the book's full text
    words_in_book = book.split()          # Split text into a list of words
    num_words = len(words_in_book)        # Count words in the list
    return num_words


def get_book_text(pathToFile):
    """
    Opens a file and returns its full text as a string.
    """
    with open(pathToFile) as f:
        text = f.read()
    return text


def get_num_characters(pathToFile):
    """
    Reads a book file and returns a dictionary of character counts.
    - Keys are characters (letters, symbols, spaces, etc.)
    - Values are the number of times each character appears
    """
    book = get_book_text(pathToFile) 
    character_dict = {}

    # Loop through each character in lowercase form
    for char in book.lower():
        # If char already exists, increment by 1; otherwise start at 1
        character_dict[char] = character_dict.get(char, 0) + 1

    return character_dict


def sort_on(items):
    """
    Helper function for sorting dictionaries.
    Returns the 'num' value (frequency count).
    """
    return items['num']


def generate_report(pathToFile):
    """
    Generates and prints a formatted analysis report of a book:
    - Total word count
    - Character frequency (letters only, sorted by frequency)
    """
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {pathToFile}...')

    # Word count section
    print('----------- Word Count ----------')
    print(f"Found {get_num_words(pathToFile)} total words")

    # Character frequency section
    print("--------- Character Count -------")
    characters = get_num_characters(pathToFile)
    dict_list = []

    # Convert dictionary into a list of {char, num} objects, letters only
    for key, val in characters.items():
        if key.isalpha():  # Only include alphabetic characters
            dict_list.append({"char": key, "num": val})

    # Sort characters by frequency (highest first)
    dict_list.sort(reverse=True, key=sort_on)

    # Print each character and its count
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
