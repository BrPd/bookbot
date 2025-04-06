# counts no. of words in the book. Accepts a singular string
def count_words(book_text):
    text_list = book_text.split()  # .split() => splits the string on a delimiter
    word_count = 0
    for i in text_list:
        word_count += 1
    return word_count

# counts no. of characters in the book. Accepts a single string 
#Returns a dictionary with char-count (key-value) pair.
def count_chars(text):
    char_dict = {}
    for i in text:
        char = i.lower()    # we want uppercase characters to be also counted as lowercase to avoid duplicates
        if char not in char_dict: # set char count = 0 for first timers
            char_dict[char] = 0
        char_dict[char] += 1 
    return char_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

# Accepts a char: count dictionary. Returns a sorted list of dictionaries, wherein 
# each dictionary contains 2 key-value pair, 1 for the character and 1 for it's count. 
# For eg: list = [
#           {"char": 'e', "count": 44538}, 
#           {"char": 't', "count": 29493}, 
#           {"char": 'a', "count": 25894}
#        ]
def sorted_list_of_dict(dict):
    list = []
    for i in dict:
        list_dict = {}
        list_dict["char"] = i
        list_dict["count"] = dict[i]
        list.append(list_dict)
    list.sort(reverse=True, key=sort_on)
    return list






