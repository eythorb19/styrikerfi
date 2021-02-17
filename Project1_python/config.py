import collections

#   Settings

#   Set this to true to get logs. Set to false to only get required output parameters.
DEBUG = False

#   Set this to true if you´re reading input from 1 specific file. Set the filepath
FILEINPUT = True
filepath = 'io/in_1'

#   Error in 6 - virkar ef ég releasa resource á timeout process
#   Wrong output in 7


def log(s):
    '''Used for debugging.'''
    if DEBUG:
        print(s)

def display(s):
    '''Used for running.'''
    if DEBUG == False:
        print(s, end =" ")


def getInput():
    if FILEINPUT:

        file1 = open(filepath, 'r')
        lines = file1.readlines()

        fileInput = collections.deque()
        for line in lines:
            if line != "\n":
                fileInput.append(line)
        
        return fileInput

    