def get_num_words(frankenstein_text):
# Function defined to count the words in a book
    num_words = None
    words_list = frankenstein_text.split() # split text into a list
    num_words = len(words_list) # get through the list and find the number of words
    print(f"Found {num_words} total words")
    return num_words

def get_num_chars(frankenstein_text):
# Function defined to count the characters in a book
    frankenstein_text = frankenstein_text.lower() # converts the book to lower case to be read by the function
    # print(frankenstein_text)
    num_chars_dict = {}
    for char in frankenstein_text:
        if char in num_chars_dict:
            num_chars_dict[char] += 1
        else:
            num_chars_dict[char] = 1
    print(f"Found this number characters: {num_chars_dict}.")
    return num_chars_dict
    