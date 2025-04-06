import sys         # The built in sys module provides access to command line arguments.
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
    print(f"Analyzing book found at {filepath}...")
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


# To check if user input has less than two entries
if len(sys.argv) < 2:   # sys.argv is a list of strings representing the arguments passed to the script.
    print("invalid Input")  # The first argument is the script name, the rest are the arguments
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)     # Exits the program with a status code of 1

for i in range(1, len(sys.argv)):  # calls main() for each filepath in the user input 
    filepath = sys.argv[i]
    main()

