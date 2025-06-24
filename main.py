from stats import get_num_words, get_sorted_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_book_report(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    sorted_chars = get_sorted_chars(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_report(sys.argv[1])

main()