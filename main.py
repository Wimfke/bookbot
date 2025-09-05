from stats import count_words, num_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_dict = num_char(text)
    sorted_letters = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(letter["char"] + ":", letter["num"])
    print("============= END ===============")
    

main()