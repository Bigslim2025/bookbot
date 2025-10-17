from stats import get_num_words, get_num_chars, get_sorted_chars
from library import book_path


def main():
    # Function called to count the number of words in a book
    get_num_words(book_path)

    # The variable below stores the function defined in 'get_num_chars'
    char_counts = get_num_chars(book_path)
    # The funtion when called needs to come from the variable defined above 
    
    # for the function work as intended when called it bellow
    get_sorted_chars(char_counts)
    

if __name__ == "__main__":
    main()
