def count_words(book_text):
    text_list = book_text.split()
    word_count = 0
    for i in text_list:
        word_count += 1
    return word_count