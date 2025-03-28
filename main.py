from stats import word_counter, character_counter, sorted_char_list
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as book:
            book_contents = book.read()
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid path.")
        sys.exit(1)

    return book_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    word_count = word_counter(book_contents)
    character_count = character_counter(book_contents)
    sorted_chars = sorted_char_list(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()