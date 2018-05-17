# pythonic3.py
# based on: https://www.youtube.com/watch?v=x3v9zMX1s4s&t=1s

# Duck Typing and Easier to ask forgiveness then persmission (EAFP)

# Example from the Python Docs

import os

my_file = '/tmp/test.txt'

# Race Condition
#if os.access(my_file, os.R_OK):
#    with open(my_file) as f:
#        print(f.read())
#else:
#    print('File can not be accessed!')

# No Race Condition
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed!')
else:
    with f:
        print(f.read())
