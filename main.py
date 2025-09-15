from stats import (
    get_number_of_words, 
    get_chars_dict, 
    chars_dict_to_sorted_list
)
    

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #text = "This is a Test"
    
    num_words = get_number_of_words(text)
    char_dictionary = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dictionary)
    #print(sorted_char_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")
    
    

main()