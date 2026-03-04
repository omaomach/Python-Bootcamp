import os

def delete_tmp_files():
    files = os.listdir('.')
    tmp_files = [filename for filename in files if filename.endswith('.tmp')]

    if not tmp_files:
        print("No .tmp files found in the current directory.")
        return
    
    for file in tmp_files:
        os.remove(file)
        print(f"Deleted: {file}")

    print(f"\nDone! {len(tmp_files)} .tmp file(s) deleted.")


if __name__ == "__main__":
    delete_tmp_files()