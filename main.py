from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_location = "books/frankenstein.txt"
    text = get_book_text(file_location)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    print(f"Found {num_words} total words")
    for char in chars_dict:
        print(f"'{char}': {chars_dict[char]}")

main()