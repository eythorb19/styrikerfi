import collections
#-----------------------------------------------
# ------    OUTPUT/PRINT SETTINGS START ----------
#   DEBUG = True: All logs will be shown. 
#   DEBUG = False: Only relevant output is shown.
# ------------------------------------------------
DEBUG = True

def log(s):
    '''Used for debugging.'''
    if DEBUG:
        print(s)

def display(s):
    '''Used for running.'''
    if DEBUG == False:
        print(s, end =" ")

#--------------------------------------------------------
# ------   FILE INPUT SETTINGS START ----------------------

initFilePath = 'io/init'
inputFilePath = 'io/input'

def getInput(filepath):
    '''Get input from file input.txt, or file specified in config in case of testrun.'''
    fileInput = collections.deque()

    #   INPUT FILE PATH SPECIFIED ABOVE  ***
    file = open(filepath, 'r')
    lines = file.readlines()
    
    #   Create a queue
    for line in lines:
        if line != "\n":
            fileInput.append(line.rstrip())

    return fileInput