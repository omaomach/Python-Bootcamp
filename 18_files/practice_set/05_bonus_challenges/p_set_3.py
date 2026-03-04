import os
import argparse

def get_folder_size(folder):
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' not found")
        return
    
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a folder")
        return
    
    files = os.listdir(folder)
    total_size = 0

    for filename in files:
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            total_size = os.path.getsize(filepath)

    print(f"Total size of '{folder}': {total_size} bytes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the total size of all files in a folder")
    parser.add_argument("folder", help="The folder to calculate size for")
    args = parser.parse_args()

    get_folder_size(args.folder)

# python3.13 p_set_3.py ../05_bonus_challenges
# python3.13 p_set_3.py ../01_file_input_output_basics