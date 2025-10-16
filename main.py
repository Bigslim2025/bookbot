from stats import get_num_words
from stats import get_num_chars
from library import frankenstein_text


def main():
    # Function called to count the number of words in a book
    get_num_words(frankenstein_text)
    get_num_chars(frankenstein_text)

if __name__ == "__main__":
    main()
