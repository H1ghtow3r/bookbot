def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def get_number_of_words(text):
    words = text.split()
    return len(words)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    print(f"{num_words} words found in the document")

 
main()