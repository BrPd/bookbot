def get_book_txt(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_txt(filepath))


filepath = "./books/frankenstein.txt"
main()

