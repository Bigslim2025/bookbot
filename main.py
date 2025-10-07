def main():
# Function defined to read the content of a book
    text = get_book_text("./books/frankenstein.txt") # variable filled with the text read above
    # print(text) # command to print the text
    get_num_words(text) # call the function

def get_book_text(book_path): 
# Function defined to read the content of a book
    with open(book_path,'r', encoding="utf-8") as file_contents:
        return file_contents.read()

def get_num_words(text):
# Function defined count the words in a book
    num_words = None
    words_list = text.split() # split text into a list
    num_words = len(words_list) # get through the list and find the number of words
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
