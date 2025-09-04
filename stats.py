def count_words(text):
    return len(text.split())

def num_char(text):
    words = (text.lower()).split()
    char_dict = {}
    for word in words:
        for char in word:
            if not char in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict