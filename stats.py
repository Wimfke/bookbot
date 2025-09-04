def count_words(text):
    return len(text.split())

def num_char(text):
    char_dict = {}
    for char in text.lower():
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict