

def count_words(book_text):
    num_words = 0
    text = book_text.split()
    for word in text:
        num_words += 1
    return num_words


def get_char_numbers(book_text):
    char_dict = {}
    text = book_text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_char_numbers(dict_of_chars):
    char_list = []
    for char, count in dict_of_chars.items():
        if char.isalpha():
            char_list.append({char: count})

    def get_count(dict):
        return list(dict.values())[0]

    char_list.sort(reverse=True, key=get_count)
    
    for letter in char_list:
        for character, count in letter.items():
            print(f"{character}: {count}")
   