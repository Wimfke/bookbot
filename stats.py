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

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    letters = []
    for key in dict:
        split = {}
        split["char"] = key
        split["num"] = dict[key]
        letters.append(split)
    letters.sort(reverse=True, key=sort_on)
    return letters