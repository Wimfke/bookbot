from stats import count_words, num_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    char_dict = num_char(text)
    print(f"{word_count} words found in the document")
    print(char_dict)

main()