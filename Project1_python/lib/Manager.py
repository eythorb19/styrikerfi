import constants.priority as priority
from lib.PCB import PCB
from lib.RCB import RCB
import collections

class Manager:
    def __init__(self):
        self.PCBn = collections.deque()     #   Linked list of PCB´s
        self.RCBn = [None]*4                    #   Array of resources 0,1,2,3
        self.RL = collections.deque()       #   Ready list

        #   Initialize RCB

        for i in range(4):
             self.RCBn[i] = RCB()
        
        #   TODO: REMOVE DEBUG
        for i in range(4):
            print("Resource " + str(i) + " in state " + str(self.RCBn[i]._state))

        #   Start first process
        rootProcess = PCB(None, priority.HIGH)

        #   Add root process to the PCB and the Ready list
        self.PCBn.append(rootProcess)
        self.RL.append(rootProcess)
        print("Process 0 created")
        
    def create(self):
        process = PCB()


        print("Process  created")

    def destroy(self):
        print("Process destroyed")

    def request(self):
        print("Resource requested")

    def release(self):
        print("Resource released")

    def timeout(self):
        print("Timeout")    #   In here?
        
    def shcheduler(self):
        print("Calling scheduler")

    def init(self):

        for i in range(0,4):
            self.RCBn

        print("Initialize")

    def execute(self, cmd, index):

        if cmd == "in":
            self.init()
        
        #   Create process 
        elif cmd == "cr":
            self.create(words[1])   

        #   Destroy process
        elif cmd == "de":
            self.destroy(words[1])

        #   Reqqueset resource 
        elif cmd == "rq":
            self.request(words[1])

        elif cmd == "rl":
            self.release(words[1])

        elif cmd == "to":
            self.timeout()

        else:
            print("Invalid Input command.")

