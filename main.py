from stats import count_words

def get_book_txt(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_txt(filepath)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")


filepath = "./books/frankenstein.txt"
main()

