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


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for item in num_chars_dict:
        if (item.isalpha()):    
            char_dict = {"char": item, "num": num_chars_dict[item]}
            sorted_list.append(char_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list


