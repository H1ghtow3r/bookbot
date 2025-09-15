def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    counts = {}

    for char in text:
        lowered = char.lower()
        if lowered in counts:
            counts[lowered] += 1
        else:
            counts[lowered] = 1
    
    return counts


def sort_on(items):
    return items["num"]


def get_sorted_dict(items):
    list_of_char_dictionaries = []

    for item in items:
        if (item.isalpha()):    
            char_dict = {"char": item, "num": items[item]}
            list_of_char_dictionaries.append(char_dict)
    
    list_of_char_dictionaries.sort(reverse=True, key=sort_on)
    
    return list_of_char_dictionaries


