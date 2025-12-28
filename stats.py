def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    dict_list = []
    for char in char_dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = char_dict[char]
        dict_list.append(new_dict)
        
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list