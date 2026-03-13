# A qr code is a 2D bar code that stores data like urls, text, contact information, wifi credentials or even small chunks of JSON

'''
We are going to use a Python library like qrcode and convert url to qr
'''

import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not (filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)