def get_book_txt(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    text_list = book_text.split()
    word_count = 0
    for i in text_list:
        word_count += 1
    return word_count

def main():
    text = get_book_txt(filepath)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")


filepath = "./books/frankenstein.txt"
main()

