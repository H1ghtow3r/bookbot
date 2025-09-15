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