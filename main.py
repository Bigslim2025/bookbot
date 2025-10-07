
def get_book_text(book_path): 
# Function defined to read the content of a book
    with open(book_path,'r', encoding="utf-8") as file_contents:
        return file_contents.read()

def main():
# variable filled with the text read above
    text = get_book_text("./books/frankenstein.txt") 
    print(text) # command to print the text

main()