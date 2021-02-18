import collections
import fileinput

#   Set this to true to get logs. Set to false to only get required output parameters.
DEBUG = False

def log(s):
    '''Used for debugging.'''
    if DEBUG:
        print(s)

def display(s):
    '''Used for running.'''
    if DEBUG == False:
        print(s, end =" ")


#   ***   IF TESTRUN = TRUE: 
#           INPUT FILE IS SPECIFIED BELOW IN filepath

#   ***   IF TESTRUN = FALSE: 
#               DEFAULT INPUT FILE IS input.txt
TESTRUN = False
filepath = 'io/in_1'

#   Set this to true for run-time input
REALTIMEinput = False

def getInput():
    '''Get input from file specified in config.'''
    fileInput = collections.deque()

    #   INPUT FILE PATH SPECIFIED ABOVE  ***
    if TESTRUN:
        file1 = open(filepath, 'r')
        lines = file1.readlines()
    
    #   INPUT IS DEFAULT INPUT.TXT (if make cmd is used)
    else: 
        lines = fileinput.input()
    
    #   Create a queue
    for line in lines:
        if line != "\n":
            fileInput.append(line.rstrip())

    return fileInput




    