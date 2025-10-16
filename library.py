from reader import get_book_text

# Stores the books (or the book) to be read.
# For this release only one book is stored, 
# read and called to fulfil the requirements of the assignemnt

frankenstein_text = get_book_text("./books/frankenstein.txt")
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")