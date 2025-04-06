from stats import count_words
from stats import count_chars
from stats import sorted_list_of_dict

# opens the file and reads it's contents into a string
def get_book_txt(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    text = get_book_txt(filepath)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    
    print("--------- Character Count -------")
    char_count_dict = count_chars(text)             # to count book characters
    list = sorted_list_of_dict(char_count_dict)     # to sort(high => low) characters acc. to their count
    for i in list:
        if i['char'].isalpha() == True:             # only print if the character is an alphabet
            print(f"{i['char']}: {i['count']}")

    print("============= END ===============")




filepath = "./books/frankenstein.txt"
main()

