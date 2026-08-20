# A qr code is a 2D bar code that stores data like urls, text, contact information, wifi credentials or even small chunks of JSON

'''
We are going to use a Python library like qrcode and convert url to qr
'''

# Use pip install "qrcode[pil]" to intall the library alongside pillow for more image functionality.
import qrcode
from urllib.parse import urlparse

def is_url(value):
    try:
        parsed = urlparse(value)
    except ValueError:
        return False
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

def prompt_url(message):
    while True:
        value = input(message).strip()
        if is_url(value):
            return value
        print("That doesn't look like a URL. Include http:// or https:// (e.g. https://example.com).")

def promp_nonempty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

url = prompt_url("Enter you url: ")

# while not url:
#     url = input("Url cannot be empty. Enter a valid URL: ").strip()

filename = promp_nonempty("Filename you want to save it as: ")

# while not filename:
#     filename= input("Filename cannot be empty. Please enter a valid filename: ").strip()

if not filename.lower().endswith(".png"):
    filename = filename + ".png"

img = qrcode.make(url)

try:
    img.save(filename)
except OSError as e:
    print(f"Couldn't save to {filename}: {e}")
    raise SystemExit(1)

print(f"QR code saved to {filename}")