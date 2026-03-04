import argparse

def to_uppercase(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            contents = f.read()
        
        with open(output_file, 'w') as f:
            f.write(contents.upper())

        print(f"Done! Uppercase version saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert all words in a file to uppercase")
    parser.add_argument("input_file", help="The file to read from")
    parser.add_argument("output_file", help="The file to write the uppercase version to")
    args = parser.parse_args()

    to_uppercase(args.input_file, args.output_file)