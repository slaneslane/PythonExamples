# contextmanager.py
# based on: https://www.youtube.com/watch?v=-aKFBoZpiqA&t=469s

# old version example:
#f = open('sample.txt', 'w')
#f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
#f.close()

# new version example:
#with open('sample.txt', 'w') as f:
#    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')


# contextmanager - how does it works:
#class Open_File():
#
#    def __init__(self, filename, mode):
#        self.filename = filename
#        self.mode = mode
#
#    def __enter__(self):
#        self.file = open(self.filename, self.mode)
#        return self.file
#
#    def __exit__(self, exc_type, exc_val, traceback):
#        self.file.close() 
#
#
#with Open_File('sample.txt', 'w') as f:
#    f.write('Testing')
#
#print(f.closed) #shall return True


# another example with existing contextmanager decorator and generator:
#from contextlib import contextmanager
#
#@contextmanager
#def open_file(file, mode):
#    try:
#        f = open(file, mode)
#        yield f
#    finally:
#        f.close()
#
#with open_file('sample.txt', 'w') as f:
#    f.write('contextlib example with try-finally')
#
#print(f.closed)


# yet another example without contextmanager:
#import os
#
#cwd = os.getcwd()
#os.chdir('Sample-Dir-One')
#print(os.listdir(os.getcwd()))
#os.chdir(cwd)
#
#cwd = os.getcwd()
#os.chdir('Sample-Dir-Two')
#print(os.listdir(os.getcwd()))
#os.chdir(cwd)

# changing above example to contextmanager using generator:
from contextlib import contextmanager
import os

@contextmanager
def chdir(dirname):
    try:
        cwd = os.getcwd()
        os.chdir(dirname)
        yield 
    finally:
        os.chdir(cwd)
    
with chdir('Sample-Dir-One'):
    print(os.listdir(os.getcwd()))

with chdir('Sample-Dir-Two'):
    print(os.listdir(os.getcwd()))
