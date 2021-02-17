import constants.priority as PRIORITY
from lib.Manager import Manager
from config import log, getInput, display
import config 
import collections


def main():
  
    fileInput = getInput()

    while True:

        #   If input from file -- Go to config file to set fileInput = True and the path!
        if fileInput!= None and len(fileInput) !=0:
            userInput = fileInput.popleft()

        # wait for cmd line input
        else:
            userInput = input()         #   cmd <i>

        words = userInput.split()
        cmd = words[0]
        log("")
        for i in range(len(words)):
            log(words[i])

        #   Error check input
        if (cmd == "cr" or cmd =="de" or cmd == "rq" or cmd == "rl") and len(words) !=2:
                log("error: parameter missing")
                print("-1")
        
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
                output = manager.release(int(words[1]), -2)

            #   Timeout
            elif cmd == "to":
                output = manager.timeout()

            else:
                log("Invalid input command")
                print(str(-1) + " ")
            
            display(str(output))


if __name__ == "__main__":
    main()
