def get_num_words(book_path):
# Function defined to count the words in a book
    num_words = None # necessary for the rest of the function
    words_list = book_path.split() # split text into a list
    num_words = len(words_list) # get through the list and find the number of words
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    return num_words # to send the function to the main

def get_num_chars(book_path):
# Function defined to count the characters in a book
    # print(book_path) # cheks if uppercase is still applied (comment out as soon as debugged)
    book_path = book_path.lower() # converts the book to lower case to be read by the function
    # print(book_path) # cheks if the lower case is applied (comment out as soon as debugged)
    num_chars_dict = {} # necessary for the rest of the function 
    # loop used to transform the dictionary into a list
    for char in book_path:
        if char in num_chars_dict:
            num_chars_dict[char] += 1
        else:
            num_chars_dict[char] = 1
    print("--------- Character Count -------")
    return num_chars_dict # to send the function to the main

def get_sorted_chars(num_chars_dict):
# Function to sort the characters and print the layout as requested
    # create a list from the dictionary to be used to print the requirements
    sorted_chars = [{"char":char, "num":count} 
                    for char, count in num_chars_dict.items()] # using a 'list comprehension' instead of 'loop and append'
    sorted_chars.sort(key=lambda item: item["num"], reverse=True)
    # loop for print each character and its count from your sorted list of dictionaries
    for entry in sorted_chars:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha() or char in {'æ', 'â', 'ê', 'ë', 'ô'}:
            print(f"{char}: {num}")
    print("============= END ===============")
    return sorted_chars # to send the function to the main