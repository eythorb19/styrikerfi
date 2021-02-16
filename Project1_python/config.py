import collections

#   Settings
DEBUG = False
FILEINPUT = True
filepath = 'sample-input.txt'

def log(s):
    '''Used for debugging.'''
    if DEBUG:
        print(s)

def getInput():
    if FILEINPUT:

        file1 = open(filepath, 'r')
        lines = file1.readlines()

        fileInput = collections.deque()
        for line in lines:
            if line != "\n":
                fileInput.append(line)
        
        return fileInput