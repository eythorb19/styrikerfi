import constants.priority as PRIORITY
import constants.states as STATE
from config import log
from lib.PCB import PCB
from lib.RCB import RCB
import collections

class Manager:
    def __init__(self):
        self.PCBn = [None]*16               #   Array of PCBs
        self.RCBn = [None]*4                #   Array of resources 0,1,2,3
        self.RLn = [None]*3                 #   Array of ready lists
        self.context = PRIORITY.LOW         #   Priority context. Changes if context switch.
        self.PCBcount = 1                   #   Processes in the PCBn 

        #   Initialize RCB
        for i in range(len(self.RCBn)):
            newRcb = RCB()
            self.RCBn[i] = newRcb

        #   Initialize RL
        for i in range(len(self.RLn)):
            self.RLn[i] = collections.deque()
        
        #   Create root process - no parent
        rootProcess = PCB(None, 0)
        self.PCBn[0] = rootProcess      #   Append the PCB of the rootProcess to the PCBarray
        self.RLn[0].append(0)           #   Append the index of the PCB to the Ready List at priority 0
        log("process 0 running")


    def create(self, priority):
        '''Creates a new process with priority 0,1,2.'''

        #   Error check the priority
        if not (PRIORITY.LOW <= int(priority) <= PRIORITY.HIGH):
            log("Error: Priority should be 0,1 or 2.")
            return -1

        #   Get the ID of the currently running process (parent)
        if self.PCBcount != 0:  #  If not first process
            parentId = self.__runningProcess()          
        else:
            parentId = None

        #   First free column in the PCB array -> ID of the new process
        processId = self.__getFreeColumnPCB()       

        #   If PCB array is full
        if processId == -1:
            log("Error: Max processes reached.")
            return -1
        
        #   Create a new process with parent = parentId
        process = PCB(parentId,priority)              

        #   Add the new process to the PCB array
        self.PCBn[processId] = process                 

        #   Append the process to the childrens list of it´s parent
        if self.PCBcount !=0:  #  If not first process
            self.PCBn[parentId].children.append(processId)   

        #   Insert process into ready list
        self.RLn[priority].append(processId)          

        #   Increment PCBcount
        self.PCBcount+=1       

        log("process " + str(processId) + " created" )   #   Display process j created

        #   Call scheduler
        self.__scheduler()
        return self.__runningProcess()    


    def destroy(self, processId):
        '''Destroys a currently running process or a child.'''

        #   Count of processes before deletion
        processCount = self.PCBcount

        #   Check if trying to delete root process
        if processId == 0:
            log("Can not delete root process.")
            log("error")
            return -1

        if processId != self.__runningProcess():        
            log("Not destroying self.")

            #   Check if the process is a child of currently running process
            if self.PCBn[self.__runningProcess()].children.count(processId) == 0:
                log("Not destroying child.")
                return -1
            
            log("Destroying child ")
            
        #   Delete process and children recursively
        self.__destroyRecur(processId, self.PCBn[processId].parent)

        #   Log how many processes were destroyed
        log(str(processCount - self.PCBcount) + " processes destroyed.")
        
        self.__scheduler()
        return self.__runningProcess()



    def request(self, resourceId):
        '''Running process requests a resource'''

        #   Resource doesn´t exists
        if resourceId > len(self.RCBn)-1:
            log("Error: Resource doesn´t exist.")
            return -1

        #   Already has this resource
        if self.PCBn[self.__runningProcess()].resources.count(resourceId) > 0:
            log("Error: Resource " + str(resourceId) + " already allocated to process " + str(self.__runningProcess()))
            return -1

        #   Resource is FREE
        if self.RCBn[resourceId].state == STATE.FREE:
            self.RCBn[resourceId].state = STATE.ALLOCATED               #   Set resource state to allocated
            self.PCBn[self.__runningProcess()].resources.append(resourceId)    #   Insert resource r into list of resources of running process
            
            log("Resource " + str(resourceId) +  " allocated to process " + str(self.__runningProcess()))

        #   Process is BLOCKED
        else:
            self.PCBn[self.__runningProcess()].state = STATE.BLOCKED
            blockedId = self.RLn[self.context].popleft()
            self.RCBn[resourceId].waitList.append(blockedId)   #   Move process from ready list to waitlist

            log("process blocked")
        
        self.__scheduler()
        return self.__runningProcess()
        


    def release(self, resourceId, processId=None):
        '''Currently running process relases a resource.'''

        #   If called from the shell
        if processId == None:
            processId = self.__runningProcess()

        #   Throw error if process not holding resource
        if self.PCBn[processId].resources.count(resourceId) == 0:
            log("Process not holding resource " + str(resourceId))
            log("error")
            return -1

        #   Remove resource from resource list of running process
        self.PCBn[processId].resources.remove(resourceId)

        #   If resource waitlist is empty, set state free
        if len(self.RCBn[resourceId].waitList) == 0:
            self.RCBn[resourceId].state = STATE.FREE

        #   Else assign resource to next process on waitlist
        else:
            nextProcessId = self.RCBn[resourceId].waitList.popleft()    #   Pop first process on resource WL
            priority = self.PCBn[nextProcessId].priority                #   Get the priority of the process
            self.RLn[priority].append(nextProcessId)                    #   Add to corresponding RL
            self.PCBn[nextProcessId].resources.append(resourceId)       #   Add resource to processes resources
            self.PCBn[nextProcessId].state = STATE.READY
            
            log("Resource " + str(resourceId) + " released. Belongs now to process " + str(nextProcessId))
        
        self.__scheduler()
        return self.__runningProcess()


    def timeout(self):
        '''Time-sharing function. Stop currently running process and add to the back of RL.'''

        self.RLn[self.context].append(self.RLn[self.context].popleft())
        
        self.__scheduler()
        return self.__runningProcess()


#   ----------  PRIVATE ---------------

    def __scheduler(self):
        '''Allow first process on Ready list to run'''

        #   Check each Ready List
        for i in range(int(PRIORITY.HIGH), int(PRIORITY.LOW),-1):

            currentEmpty = (len(self.RLn[self.context]) == 0)

            #   If something on RL and current priority context lower, or - if current context RL empty
            if (len(self.RLn[i]) > 0) and (self.context < i or currentEmpty):     
                self.__contextSwitch(i)                                             #   Perform context switch
                log("Context switch to priority " + str(i))
                break
        
        log("Process " + str(self.__runningProcess()) + " running.")

    def __runningProcess(self):
        '''Returns the current running process'''
        return self.RLn[self.context][0]


    def __contextSwitch(self, context):
        '''Perform context switch'''
        self.context = context


    def __destroyRecur(self, processId, parentId):
        '''Destroy process and it´s children recursively'''

        #   Delete PCBs of children
        if len(self.PCBn[processId].children) > 0:
            for childId in list(self.PCBn[processId].children):
                self.__destroyRecur(childId, processId)
        
        #   Remove process from parent children list
        if parentId != None:
            self.PCBn[parentId].children.remove(processId)
        
        #   Remove from ready list
        if self.PCBn[processId].state == STATE.READY:
            priority = self.PCBn[processId].priority
            self.RLn[priority].remove(processId)
        
        #   Remove from resource wait lists
        else:
            for r in range(len(self.RCBn)):
                if self.RCBn[r].waitList.count(processId) == 1:     #   If process is on ready list
                    self.RCBn[r].waitList.remove(processId)

        #   Release resources of process i
        self.__releaseResources(processId)
        
        #   Free PCB of process
        self.PCBn[processId] = None
        self.PCBcount-=1

    def __releaseResources(self, processId):
        '''Release resources of proess'''
        for r in list(self.PCBn[processId].resources):
            self.release(r, processId)

        
    def __getFreeColumnPCB(self):
        '''Returns the first free column of the PCB array'''

        for i in range(len(self.PCBn)):
            if self.PCBn[i] == None:
                return i

        return -1   #   Array full