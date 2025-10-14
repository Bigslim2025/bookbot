def get_book_text(book_path): 
# Function defined to read the content of a book
    with open(book_path,'r', encoding="utf-8") as file_contents:
        return file_contents.read()