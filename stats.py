

def count_words(book_text):
    num_words = 0
    text = book_text.split()
    for word in text:
        num_words += 1
    print(f"{num_words} words found in the document")


def get_char_numbers(book_text):
    char_dict = {}
    text = book_text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(f"{char_dict}")