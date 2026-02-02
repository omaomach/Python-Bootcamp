# Write to a file called John Doe.txt
# The file should contain data about John Doe
# You need to note that when using write "w" for writing. If the file exists, its
# contents will be overwritten. If the file doesn't exist, a new one will be created.

f = open('sample.txt', 'w')

string = '''
John Doe is a nice guy. He lives in NYC and he works with Python.
God willing, I'll also go abroad.
'''

f.write(string)

f.close()