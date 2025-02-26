import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

from stats import count_words
from stats import get_char_numbers
from stats import sort_char_numbers



def main():
    path = sys.argv
    if len(path) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(path[1]))} total words")
    print("----------- Word Count ----------")
    sort_char_numbers(get_char_numbers(get_book_text(path[1])))
    print("============= END ===============")

main()