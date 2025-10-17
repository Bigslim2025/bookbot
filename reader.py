def get_book_text(path): 
# Function defined to read the content of a book
    with open(path,'r', encoding="utf-8") as file_contents:
        return file_contents.read()