import constants.priority as PRIORITY
from lib.Manager import Manager

def main():

    #   Initialize the Manager
    manager = Manager()

    while True:
        userInput = input() #   cmd <i>

        words = userInput.split()
        cmd = words[0]

        #   Initialize the system. 
        if cmd == "in":
            manager = Manager()     #   New manager
        
        #   Create process 
        elif cmd == "cr":

            # try:
            priority = int(words[1])
            manager.create(priority)                     #   Create new process
            
            # except: 
            #     print("Priority missing")

        #   Destroy process
        elif cmd == "de":

            # try: 
            process = int(words[1])
            manager.destroy(process)
            
            # # except:
            # #     print("Process id missing")
            
        #   Reqqueset resource 
        elif cmd == "rq":
            manager.request(words[1])

        elif cmd == "rl":
            manager.release(words[1])

        elif cmd == "to":
            manager.timeout()

        else:
            print("Invalid Input command.")

if __name__ == "__main__":
    main()
