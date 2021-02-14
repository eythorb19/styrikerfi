import constants.priority as PRIORITY
import constants.states as STATE

from lib.PCB import PCB
from lib.RCB import RCB
import collections

class Manager:
    def __init__(self):
        self.PCBn = [None]*16                #   Array of PCBs
        self.RCBn = [None]*4                #   Array of resources 0,1,2,3
        self.RL = collections.deque()       #   Ready list
        self.PCBcount = 0

        #   Initialize RCB
        for i in range(4):
            self.RCBn[i] = RCB()
        
        #   Create root process - no parent
        rootProcess = PCB(None)

        #   Append the PCB of the rootProcess to the PCBarray
        self.PCBn[0] = rootProcess

        #   Append the index of the PCB to the Ready List   
        self.RL.append(0)

        #   Increment PCBcount
        self.PCBcount+=1

        print("Process 0 running ")      #   Process 0 running
    
    def create(self, priority = None):
        '''Creates a new process with priority 0,1,2.'''

        #   Error check the priority
        if not (PRIORITY.LOW <= int(priority) <= PRIORITY.HIGH):
            print("Error: Priority is 0,1 or 2.")
            return

        #   Get the ID of the currently running process (parent)
        if self.PCBcount != 0:  #  If not first process
            parentId = self.RL[0]             
        else:
            parentId = None

        #   First free column in the PCB array -> ID of the new process
        processId = self.getFreeColumnPCB()       
        
        #   Create a new process with parent = parentId
        process = PCB(parentId)              

        #   Add the new process to the PCB array
        self.PCBn[processId] = process                 

        #   Append the process to the childrens list of it´s parent
        if self.PCBcount !=0:  #  If not first process
            self.PCBn[parentId].children.append(processId)   

        #   Insert process into ready list
        self.RL.append(processId)          

        #   Increment PCBcount
        self.PCBcount+=1       

        print("process " + str(processId) + " created." )   #   Display process j created

    
    def destroyRecur(self, processId, parentId):

        #TODO: Einhver iteration villa: dequeue mutaded during iteration

        #   Get process to remove
        process = self.PCBn[processId]
        
        #   Delete PCBs of children
        if len(process.children) > 0:
            for childId in process.children:
                self.destroyRecur(childId, processId)
        
        #   Remove process from parent children list
        if parentId != None:
            self.PCBn[parentId].children.remove(processId)
        
        #   Remove from ready list
        if process.state == STATE.READY:
            self.RL.remove(processId)
        
        #   Remove from resource wait lists
        else:
            for r in range(self.RCBn):
                if self.RCBn[r].waitList.count(processId) == 1:     #   If process is on ready list
                    self.RCBn[r].waitList.remove(processId)

        #   Release resources of process i
        for r in process.resources:
            self.RCB[r].state = STATE.FREE
        
        #   Free PCB of process
        self.PCBn[processId] = None
        self.PCBcount-=1
    
    
    def destroy(self, processId):
        '''Destroys a currently running process or a child.'''

        #   Current processes
        processCount = self.PCBcount

        #   Check if process exists
        process = self.PCBn[processId]
        if process == None:
            print("No process no: " + str(processId))
            return
        
        #   Delete process and children recursively
        self.destroyRecur(processId, process.parent)

        print(str(processCount - self.PCBcount) + " processes destroyed.")

        
        # #   Check if the process is currently running or a child of a currently running process
        # # if processId != runningProcessId or self.PCBn[self.RL.index[0]].children.count(processId) == 0:
        # #     print("Currently running process, i, can destroy a child process, j, or itself (i = j)")
        
        # #   Remove process from parent children list
        # if process.parent != None:
        #     self.PCBn[process.parent].children.remove(processId)

        # #   Release resources of process i
        # for r in process.resources:
        #     self.RCB[r].state = STATE.FREE

        # #   Remove from ready list
        # if process.state == STATE.READY:
        #     self.RL.remove(processId)

        # #   TODO: Getur process verið á mörgum waitlistum hjá fleiri en 1 resource?
        # #   Remove from resource wait list
        # else:
        #     for r in range(self.RCBn):
        #         if self.RCBn[r].waitList.count(processId) == 1:     #   If process is on ready list
        #             self.RCBn[r].waitList.remove(processId)

        # #   Destroy process
        # self.PCBn[processId] = None
        # print("Process " + str(processId) + " destroyed.")

     


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

    def getFreeColumnPCB(self):
        '''Returns the first free column of the PCB array'''

        for i in range(len(self.PCBn)):
            if self.PCBn[i] == None:
                return i
                
        #   TODO: TREAT IF ARRAY IS FULL
        print("Array full")
        return