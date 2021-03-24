import constants.sizes as sizes
from settings import log
from lib.VirtualAddress import VirtualAddress
import collections

class Manager:
    def __init__(self, ST, PT):
        self.PM = [None]*(sizes.FRAME_SIZE*sizes.SEGMENT_SIZE)      #   Physical memory
        self.disk = [[None]*sizes.FRAME_SIZE]*sizes.SEGMENT_SIZE    #   Paging disk
        self.frames = collections.deque()
        self.initPM(ST,PT)                                          #   Initialize physical memory

    

    def initPM(self, ST, PT):
        '''Initializes Physical memory. Takes in ST (Segment Table) and PT (Page Table)'''

        #   Segment table
        for i in range(int(len(ST)/3)):
            ss = ST[3*i]       #    Segment ss
            zs = ST[3*i+1]     #    Size zs of segment ss
            fs = ST[3*i+2]     #    Frame fs where PT of segment ss resides in

            self.PM[2*ss] = zs  
            self.PM[2*ss+1] = fs

        #   Page table
            for j in range(int(len(PT)/3)):
                pp = PT[3*j+1]     #    Page pp of segment ss
                fp = PT[3*j+2]     #    Frame fp where page pp resides in
                self.PM[fs*sizes.FRAME_SIZE+pp] = fp


    def virtualAddressTranslation(self, VA):
        '''Translates virtual address into Physical address'''
        returnVal = ""

        log("\n")
        va = VirtualAddress(VA)
        log("VA: " + str(VA))
        log("s: " + str(va.s) + " p: " + str(va.p) + " w: " + str(va.w)  + " pw: " + str(va.pw))

        sizeOfsegmentIndex = 2*va.s
        frameNumberIndex = 2*va.s+1

        if va.pw >= self.PM[sizeOfsegmentIndex]:
            log("Error: VA is outside of the segment boundary")
            return -1

        elif self.PM[frameNumberIndex] < 0:
            log("page fault: PT is not resident")
            #   Allocate free frame f1 using list of free frames
            #   Update list of free frames
            #   Read disk block b = |PM[2s + 1]| into PM starting at location f1*512
            #   Update ST entry PM[2s+1] = f1 
        
        elif self.PM[self.PM[frameNumberIndex]*sizes.FRAME_SIZE+va.p] < 0:
            log("Page fault: page is not resident")
            #  Allocate free frame f2 using list of free frames
            #  Update list of free frames
            #  Read disk block b = |PM[PM[2s + 1]*512 + p]| into PM staring at f2*512
            #  PM[PM[2s + 1]*512 + p] = f2 /* update PT entry */

        
        pageTableIndex = self.PM[2*va.s+1]*sizes.FRAME_SIZE + va.p
        log("Page table index is: " + str(pageTableIndex))
        PA = self.PM[pageTableIndex] * sizes.FRAME_SIZE + va.w
        log("Physical address is: " + str(PA))
        return PA

    def printValues(self, segmentNo, pageFrame):
        '''Print value of segment'''
        index = 2*segmentNo
        log("Segment " + str(segmentNo) + " contains value: " + str(self.PM[index]) + " +1: " + str(self.PM[index+1]))
        log("It´s PT " + str(self.PM[self.PM[index+1]*sizes.FRAME_SIZE+pageFrame]))


    def read_block(self,b,m):
        '''Copies block D[b] into PM frame starting at location PM[m]'''
        pass
# • Paging Disk
# • emulated as a two‐dimensional integer array, D[B][512]
# • B: number of blocks (e.g., 1024)
# • 512: block size (= page size)
# • Disk may only be accessed one block at a time:
# • read_block(b, m) copies block D[b] into PM frame starting at location PM[m]

        # Demand paging
        #   Búum til annað array eða vector. 
        #   Á að representa eins og það sé veirð að sækja gögn af disk/skrá.
        #   2D integer array D[B][512] hversu mikið á að sækja