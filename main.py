def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        #print(f"{file_contents}")
        #get_char_numbers(file_contents)

from stats import count_words
from stats import get_char_numbers



def main():
    path = "/home/ajunara/workspace/github.com/bookbot/books/frankenstein.txt"
    #get_book_text(path)
    count_words(get_book_text(path))
    get_char_numbers(get_book_text(path))


main()