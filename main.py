import sys
from stats import get_num_words, get_num_chars, get_sorted_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_countes = get_sorted_counts(num_chars)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in num_chars:
        if c.isalpha():
            print(f"{c}: {num_chars[c]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_name = sys.argv[1]
    print_report(book_name)

main()
