# import sys

# def count_lines(filename):
#     try:
#         with open(filename, 'r') as f:
#             lines = f.readlines()
#         print(f"Number of lines: {len(lines)}")
#     except FileNotFoundError:
#         print(f"Error: File 'filename' not found.")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python count_lines.py <filename>")
#         sys.exit(1)

#     count_lines(sys.argv[1])

#################################################################################################

import argparse

def count_lines(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of lines in a file")
    parser.add_argument("filename", help="The file to count lines in")
    args = parser.parse_args()

    count_lines(args.filename)