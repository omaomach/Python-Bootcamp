# We have 2 types of modules in Python:
# - Built in modules
# - External modules - Can either be written by you or be installed using a utility called pip
# - https://docs.python.org/3/py-modindex.html - List of all built in python modules

import math
import os
import mymodule
import requests # used to fetch the html of online pages
import pandas

print(math.sqrt(8))
mymodule.hello()
r = requests.get('https://www.comraid.io')
print(r.text)
# h = r.headers['content-type']
# print(h)

# os.abort()