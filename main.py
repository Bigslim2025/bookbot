from stats import get_num_words

def main():
# Function defined to read the content of a book
    text = get_book_text("./books/frankenstein.txt") # variable filled with the text read above
    # print(text) # command to print the text
    get_num_words(text) # call the function

def get_book_text(book_path): 
# Function defined to read the content of a book
    with open(book_path,'r', encoding="utf-8") as file_contents:
        return file_contents.read()

if __name__ == "__main__":
    main()
