import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.lower().endswith(ext)]

    if not(os.path.exists("images")):
        os.mkdir("images")
    
    # Continue numbering from where images/ left off, so a re-run adds to the
    # collection instead of overwriting photo-1, photo-2, ...
    highest = 0
    for name in os.listdir("images"):
        if name.startswith("photo-") and name.endswith(ext):
            number = name[len("photo-"):-len(ext)]  # the bit between "photo-" and ".jpg"
            if number.isdigit():
                highest = max(highest, int(number))

    for i, file in enumerate(files_with_ext):
        new_name = f"photo-{highest + i + 1}{ext}"
        print(f"{file} -> images/{new_name}")
        os.rename(file, f"images/{new_name}")

if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files, ".jpg")
