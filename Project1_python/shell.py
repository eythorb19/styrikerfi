import constants.priority as PRIORITY
from lib.Manager import Manager
from config import log, getInput, display
import config as settings

def main():
    
    manager = Manager()
    if settings.REALTIMEinput == False:     #   IF not realtime input, and program started with python3 shell.py
        fileInput = getInput()

    while True:

#----------  COMMENT IN FOR REALTIME CMD LINE INPUT. -------------------------------
        # #  To start program: >> python3 shell.py

        # print()
        # userInput = input()         #   cmd <i>
# ------------------------------------------------------------------------


# -------------  COMMENT IN FOR FILEINPUT.  ---------------------------
        #  To start program using input.txt: >> make
        #  To start program using own file: >> python3 shell.py {filepath}

        if fileInput!= None and len(fileInput) !=0:
            userInput = fileInput.popleft()
        else:
            print()
            break
# ------------------------------------------------------------------------


#----   SHELL START --------------

        words = userInput.split()
        cmd = words[0]
        log("")
        for i in range(len(words)):
            log(words[i])

        #   Error check input
        if (cmd == "cr" or cmd =="de" or cmd == "rq" or cmd == "rl") and len(words) !=2:
                log("error: parameter missing")
                print("-1")
        
        #   Execute command
        else:
            #   Initialize the system. 
            if cmd == "in":
                manager = Manager()     #   New manager
                print()
                output = 0
            
            #   Create process 
            elif cmd == "cr":
                output = manager.create(int(words[1]))
                
            #   Destroy process
            elif cmd == "de":
                output = manager.destroy(int(words[1]))
                
            #   Request resource 
            elif cmd == "rq":
                output = manager.request(int(words[1]))

            #   Release resource
            elif cmd == "rl":
                output = manager.release(int(words[1]))

            #   Timeout
            elif cmd == "to":
                output = manager.timeout()

            else:
                log("Invalid input command")
                print(str(-1) + " ")
            
            display(str(output))


if __name__ == "__main__":
    main()
