def get_num_words(text):
# Function defined count the words in a book
    num_words = None
    words_list = text.split() # split text into a list
    num_words = len(words_list) # get through the list and find the number of words
    print(f"Found {num_words} total words")