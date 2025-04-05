def count_words(book_text):
    text_list = book_text.split()
    word_count = 0
    for i in text_list:
        word_count += 1
    return word_count

def count_chars(text):
    char_dict = {}
    for i in text:
        char = i.lower()
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1 
    return char_dict