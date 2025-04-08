from stats import get_num_words, number_of_characters, create_report
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    num_chars = number_of_characters(text)
    sorted_num_chars = create_report(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

# Print each character and its count
    for char_data in sorted_num_chars:
        char = char_data["char"]
        count = char_data["count"]
    # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
   # print(sorted_num_chars)
    #print (num_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()