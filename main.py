from stats import count_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_location = "books/frankenstein.txt"
    text = get_book_text(file_location)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    sorted_list = sort_dict(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()