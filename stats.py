def get_num_words(pathToFile):
    book = get_book_text(pathToFile)
    words_in_book = book.split()
    num_words = len(words_in_book)
    return num_words

def get_book_text(pathToFile):
    with open(pathToFile) as f:
        text = f.read()
    return text

def get_num_characters(pathToFile):
    # returns number of times each character appears (including symbols and spaces)
    book = get_book_text(pathToFile) 
    character_dict = {}
    for char in book.lower():
        character_dict[char] = character_dict.get(char, 0) + 1
    return character_dict

def sort_on(items):
    return items['num']

def generate_report(pathToFile):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {pathToFile}...')
    print('----------- Word Count ----------')
    print(f"Found {get_num_words(pathToFile)} total words")
    print("--------- Character Count -------")
    characters = get_num_characters(pathToFile)
    dict_list = []
    for key, val in characters.items():
        if key.isalpha():
            dict_list.append({"char": key, "num" : val})
        else:
            continue
    dict_list.sort(reverse=True, key=sort_on)
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")