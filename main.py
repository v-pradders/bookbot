from stats import get_book_text, get_character_count, get_report
import sys

def main():

    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_contents = get_book_text(sys.argv[1])

    book_character_counter = get_character_count(file_contents)

    book_character_counter_sorted = get_report(book_character_counter)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {len(file_contents.split())} total words")
    print("--------- Character Count -------")
    
    for dict in book_character_counter_sorted:
        print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")



main()

