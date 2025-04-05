from stats import count_words
from stats import count_chars

def get_book_txt(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_txt(filepath)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    char_count_dict = count_chars(text)
    print(char_count_dict)


filepath = "./books/frankenstein.txt"
main()

