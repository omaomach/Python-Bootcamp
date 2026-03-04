import argparse

def search_word(filename, word):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
        count = contents.lower().split().count(word.lower())
        print(f"'{word}' appears {count} time(s) in {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search how many times a word appears in a file")
    parser.add_argument("filename", help="The file to search in")
    parser.add_argument("word", help="The word to search for")
    args = parser.parse_args()

    search_word(args.filename, args.word)