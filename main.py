from stats import get_number_of_words, get_chars_dict, get_sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #text = "This is a Test"
    
    num_words = get_number_of_words(text)
    char_dictionary = get_chars_dict(text)
    sorted_char_dict = get_sorted_dict(char_dictionary)
    #print(sorted_char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_dict:
        print(f"{item['char']}: {item['num']}")

 
main()