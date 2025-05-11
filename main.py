def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main ():
    text = get_book_text("books/frankenstein.txt")
    number_words(text)
    number_characters(text)
    
from stats import number_words
from stats import number_characters

main ()
