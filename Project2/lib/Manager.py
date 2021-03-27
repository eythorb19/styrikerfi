#   Author: Eyþór Óli Borgþórsson
#   Email: eythorb19@ru.is
#   Date: 27.3.2021

import constants.sizes as sizes
from settings import log
from lib.VirtualAddress import VirtualAddress

class Manager:
    ''' Manager of Physical memory and disk. Performs Virtual Address Translation'''

    def __init__(self, ST, PT):
        self.PM = [0]*(sizes.FRAME_SIZE*sizes.SEGMENT_SIZE)      #   Physical memory
        self.frames = [False]*sizes.SEGMENT_SIZE                 #   Array keeping track of occupied frames, False = free

        #   Frames 0 and 1 occupied for segment table
        self.frames[0] = True
        self.frames[1] = True

        #   Initialize paging disk
        self.disk = [None]*sizes.BLOCK_QTY
        for i in range(sizes.BLOCK_QTY):
            block = [0]*sizes.BLOCK_SIZE
            self.disk[i] = block

        #   Initialize physical memory
        self.initPM(ST,PT)

        #   Log contents of disk and PM
        log("\n INIT STATE OF DISK AND PM")
        self.printPM()
        self.printDisk()

    def initPM(self, ST, PT):
        '''Initializes Physical memory. Takes in ST (Segment Table) and PT (Page Table)'''

        segments = int(len(ST)/3)       #   Number of segments
        pages= int(len(PT)/3)           #   Number of pages
        
        #   Segment table
        for i in range(segments):
            ss = ST[3*i]            #    Segment ss
            zs = ST[3*i+1]          #    Size zs of segment ss
            fs = ST[3*i+2]          #    Frame fs where PT of segment ss resides in

            self.PM[2*ss] = zs      #   Insert segment size into segment table
            self.PM[2*ss+1] = fs    #   Insert frame of PT into segment table

            self.frames[fs] = True  #   Set frame occupied

        #   Page table
        for i in range(pages):
            sp = PT[3*i]            #    Segment sp
            pp = PT[3*i+1]          #    Page pp of segment ss
            fp = PT[3*i+2]          #    Frame fp where page pp resides in
            fs = self.PM[2*sp+1]    #   Frame fs where PT of segment ss resides in

            if fs >= 0:
                self.PM[fs*sizes.FRAME_SIZE+pp] = fp        #   Insert frame number into Page Table
                self.frames[fp] = True                      #   Set frame occupied

            else:
                self.disk[abs(fs)][pp] = fp                 #   Write frame number to disk at block fs, page pp

    def virtualAddressTranslation(self, VA):
        '''Translates virtual address into Physical address'''

        va = VirtualAddress(VA)                              #   Break VA into components s,p,w,pw
        self.displayComponents(va)
        
        #   VA outside segment boundary
        if va.pw >= self.getSegmentSize(va.s):
            log("Error: VA is outside of the segment boundary")             
            return -1

        #   PT not resident: Page Fault
        elif self.getFrameNumberPT(va.s) < 0:
            log("page fault: PT is not resident")

            freeFrame = self.getFreeFrame()                                                 #   Free frame allocated, and frame marked occupied
            self.readBlock(abs(self.getFrameNumberPT(va.s)), freeFrame*sizes.FRAME_SIZE)    #   Read disk block b = |PM[2s + 1]| into PM starting at location f1*512
            self.PM[self.getFrameNumberIndex(va.s)] = freeFrame                             #   Update ST entry PM[2s+1] = f1
        
        #   Page not resident: Page Fault
        elif self.getPageofPT(va.s, va.p) < 0:
            log("Page fault: page is not resident")

            freeFrame = self.getFreeFrame()                                                 #   Free frame allocated, and frame marked occupied
            self.readBlock(abs(self.getPageofPT(va.s, va.p)), freeFrame)                    #  Read disk block b = |PM[PM[2s + 1]*512 + p]| into PM staring at f2*512                  
            self.PM[self.getPageIndex(va.s, va.p)] = freeFrame                              #   Update PT entry PM[PM[2s + 1]*512 + p] = f2

        #   Calculate and return physical address
        log("PHYSICAL ADDRESS is: " + str(self.getPhysicalAddress(va.s, va.p, va.w)) + "\n")
        return self.getPhysicalAddress(va.s, va.p, va.w)


    #   ---------------------------
    #   HELP FUNCTIONS
    #   ---------------------------

    def getSegmentSizeIndex(self,s):
        ''' Returns segment size index'''
        return 2*s

    def getFrameNumberIndex(self,s):
        ''' Returns frame number index '''
        return 2*s+1

    def getSegmentSize(self, s):
        ''' Get size of segment s.'''
        return self.PM[self.getSegmentSizeIndex(s)]

    def getFrameNumberPT(self, s):
        ''' Get frame number of PT at index 2s+1'''
        return self.PM[self.getFrameNumberIndex(s)]

    def getPageIndex(self,s,p):
        ''' Get page index at self.PM[2s+1] * frame_size + p'''
        return self.getFrameNumberPT(s) * sizes.FRAME_SIZE + p

    def getPageofPT(self,s,p):
        ''' Get page of PT'''
        return self.PM[self.getPageIndex(s,p)]

    def getPhysicalAddress(self, s, p, w):
        ''' Returns physical address'''
        return self.PM[self.getPageIndex(s,p)]*sizes.FRAME_SIZE + w

    def getFreeFrame(self):
        ''' Finds free frame, marks it occupied and returns it.'''
        for i in range(len(self.frames)):
            if self.frames[i] == False:
                self.frames[i] = True
                return i

    def readBlock(self,b,m):
        '''Copies block D[b] into PM frame starting at location PM[m]. Updates ST entry'''
        block = self.disk[b]
        for i in range(len(block)):         
            if block[i] != 0:
                self.PM[m+i] = block[i]     #   Read block contents to physical memory
    

    #   ----------------------------
    #   PRINT FUNCTIONS
    #   ---------------------------

    def displayComponents(self, va):
        ''' Displays segment size, frame number, page index and page for VA translation'''
        log("------------\nVA values \n---------------")
        log(va.getVa())
        log("Segment size: " + str(self.getSegmentSize(va.s)))
        log("Frame number of PT: " + str(self.getFrameNumberPT(va.s)))
        log("Page index is: " + str(self.getPageIndex(va.s, va.p)))
        log("Page is: " + str(self.getPageofPT(va.s, va.p)))

    def printPM(self):
        ''' Prints contents of the physical memory, where values are not 0'''
        log("--------------\nPhysical memory \n--------------")
        for i in range(len(self.PM)):
            if self.PM[i] != 0:
                log(str(i) + "  |" + str(self.PM[i]) + "|")

    def printDisk(self):
        ''' Prints contents of the disk, where values are not 0'''
        log("--------------\nDisk \n---------------")
        for b in range(sizes.BLOCK_QTY):
            for f in range(sizes.BLOCK_SIZE):
                if self.disk[b][f] != 0:
                    log(str(b) + "  |" + str(self.disk[b][f]) + "|")