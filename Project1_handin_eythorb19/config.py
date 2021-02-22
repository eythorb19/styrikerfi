import collections
import fileinput

#-----------------------------------------------------------------
#---------  REAL TIME INPUT VS. FILE INPUT SETTINGS --------------
# REALTIMEinput = True: Shell waits for user to input next command
# REALTIMEinput = False: Shell takes in file input and shuts down after processing each line.  

REALTIMEinput = False
#-----------------------------------------------------------------
# ------    REAL TIME INPUT VS. FILE INPUT SETTINGS END ----------
#-----------------------------------------------------------------


#-----------------------------------------------
# ------    OUTPUT/PRINT SETTINGS START ----------
#   DEBUG = True: All logs will be shown. 
#   DEBUG = False: Only relevant output is shown.
# ------------------------------------------------
DEBUG = False

def log(s):
    '''Used for debugging.'''
    if DEBUG:
        print(s)

def display(s):
    '''Used for running.'''
    if DEBUG == False:
        print(s, end =" ")
#-----------------------------------------------
# ------    OUTPUT/PRINT SETTINGS END ----------
#-----------------------------------------------


#--------------------------------------------------------
# ------   FILE INPUT SETTINGS START ----------------------
#   TESTRUN = True: Input file is specified below in the var filepath.
#   TESTRUN = False: Input file is input.txt by default.
TESTRUN = False
filepath = 'io/in_1'    #   Input for run

def getInput():
    '''Get input from file input.txt, or file specified in config in case of testrun.'''
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

#--------------------------------------------------------
# ------   FILE INPUT SETTINGS END ------------------------
#--------------------------------------------------------
