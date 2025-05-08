import string
ENCODING = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])

print(ENCODING)

help(str)