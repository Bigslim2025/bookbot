from reader import get_book_text
from stats import get_num_words, get_num_chars, get_sorted_chars
from library import get_book_path


def main():
    
    # Feedback on the boot of the program an get the book path
    print("============ BOOKBOT ============")
    book_path = get_book_path()
    
    # Feedback on the book found an its path 
    print(f"Analyzing book found at {book_path}")
    
    # The variable stores the text called by the function
    text = get_book_text(book_path)
    
    # Function is called to count the number of words in a book
    get_num_words(text)

    # The variable below stores the function defined in 'get_num_chars',
    # The funtion when called needs to come from the variable defined 
    char_counts = get_num_chars(text)

    # Function is called and sorts the character as defined by the assignment
    get_sorted_chars(char_counts)

if __name__ == "__main__":
    main()
