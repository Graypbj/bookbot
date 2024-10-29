def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    list_of_letters = dict_to_list(num_chars)
    list_of_letters.sort(reverse=True, key=sort_on)
    print_letters(list_of_letters)

def dict_to_list(num_chars):
    list_of_chars = []
    for letter in num_chars:
        if letter.isalpha():
            list_of_chars.append({"letter": letter, "num": num_chars[letter]})
    return list_of_chars

def sort_on(list_of_chars):
    return list_of_chars["num"]

def print_letters(list_of_chars):
    for letter_num_group in list_of_chars:
        print(f"The '{letter_num_group["letter"]}' character was found {letter_num_group["num"]} times")

def get_num_chars(book_string):
    lower_string = book_string.lower()
    letter_dict = {}
    for letter in lower_string:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as book:
        return book.read()
    
main()