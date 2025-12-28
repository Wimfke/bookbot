def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def main():
    file_location = "books/frankenstein.txt"
    text = get_book_text(file_location)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()