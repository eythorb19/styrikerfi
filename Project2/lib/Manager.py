import constants.sizes as sizes
from settings import log
from lib.VirtualAddress import VirtualAddress
import collections

class Manager:
    def __init__(self, ST, PT):
        self.PM = [0]*(sizes.FRAME_SIZE*sizes.SEGMENT_SIZE)      #   Physical memory
        self.frames = [False]*sizes.SEGMENT_SIZE                    #   Array keeping track of occupied frames, False = free

        #   Frames 0 and 1 occupied for segment table
        self.frames[0] = True
        self.frames[1] = True

        #   Initialize paging disk
        self.disk = [None]*sizes.BLOCK_QTY
        for i in range(sizes.BLOCK_QTY):
            block = [0]*sizes.BLOCK_SIZE
            self.disk[i] = block
    
        self.initPM(ST,PT)                                          #   Initialize physical memory


    def initPM(self, ST, PT):
        '''Initializes Physical memory. Takes in ST (Segment Table) and PT (Page Table)'''

        #   INPUT (ST and PT)
        #-------------------------------------------------------------------------------------
        # ss_1    zs_1     fs_1      |  ss_2   zs_2   fs_2       ....   ss_i  zs_i  fs_i  #         SEGMENT TABLE [ss_1, zs_1, fs_1, ss_2 ... fs_i]
        #-------------------------------------------------------------------------------------
        # sp_11    pp_11    fp_11    |  sp_21    pp_21    fp_21    |  sp_i1    pp_i1    fp_i1 
        # sp_12    pp_12    fp_12    |  sp_22    pp_22    fp_22    |  sp_i2    pp_i2    fp_i2       PAGE TABLE  [sp_11, pp_11, fp_11, sp_12.. sp_21...fp_ij]
        #            .               |             .               |             .
        #            .               |             .               |             .
        # sp_1j    pp_1j    fp_1j    |  sp_2j    pp_2j    fp_2j    |  sp_ij   pp_ij     fp_ij

        segments = int(len(ST)/3)
        print("Segments " + str(segments))

        pages= int(len(PT)/3)
        print("Pages: " + str(pages))
        
        #   Segment table
        for i in range(segments):
            ss = ST[3*i]       #    Segment ss
            zs = ST[3*i+1]     #    Size zs of segment ss
            fs = ST[3*i+2]     #    Frame fs where PT of segment ss resides in

            self.PM[2*ss] = zs  
            self.PM[2*ss+1] = fs

            self.frames[fs] = True  #   Set frame occupied

        for i in range(pages):
            sp = PT[3*i]       #    Segment sp
            pp = PT[3*i+1]     #    Page pp of segment ss
            fp = PT[3*i+2]     #    Frame fp where page pp resides in

            fs = self.PM[2*sp+1]    #   Frame fs where PT of segment ss resides in

            if fs >= 0:
                self.PM[fs*sizes.FRAME_SIZE+pp] = fp        #   Insert frame number into Page Table
                self.frames[fp] = True                      #   Set frame occupied

            else:
                self.disk[abs(fs)][pp] = fp                      #   Write frame number to disk at block fs, page pp


    def virtualAddressTranslation(self, VA):
        '''Translates virtual address into Physical address'''
        log("\n")
        va = VirtualAddress(VA)
        log("VA: " + str(VA))
        log("s: " + str(va.s) + " p: " + str(va.p) + " w: " + str(va.w)  + " pw: " + str(va.pw))

        segmentSizeIndex = 2*va.s
        segmentSize = self.PM[segmentSizeIndex]     #   Size of segment s

        frameNumberIndex = 2*va.s+1
        frameNumberOfPT = self.PM[frameNumberIndex]     #   Frame number of Page table

        pageIndex = self.PM[frameNumberOfPT]*sizes.FRAME_SIZE+va.p    #   Index to page inside frame {frameNumberOfPT}

        #   If VA outside segment boundary
        if va.pw >= segmentSize:
            log("Error: VA is outside of the segment boundary")
            return -1

        #   If PT not resident: Page Fault
        elif frameNumberOfPT < 0:
            log("page fault: PT is not resident")

            freeFrame = self.getFreeFrame()                                 #   Free frame allocated, and frame marked occupied
            self.readBlock(abs(frameNumberOfPT), freeFrame*sizes.FRAME_SIZE)     #   Read disk block b = |PM[2s + 1]| into PM starting at location f1*512
            self.PM[frameNumberIndex] = freeFrame                           #   Update ST entry PM[2s+1] = f1
        
        #   If page is not resident: Page Fault
        elif pageIndex < 0:
            log("Page fault: page is not resident")

            freeFrame = self.getFreeFrame()                                 #   Free frame allocated, and frame marked occupied
            self.readBlock(abs(pageIndex), freeFrame)                       #  Read disk block b = |PM[PM[2s + 1]*512 + p]| into PM staring at f2*512                  
            self.PM[pageIndex] = freeFrame                                  #   Update PT entry PM[PM[2s + 1]*512 + p] = f2

        
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


    def getFreeFrame(self):
        ''' Finds free frame, marks it occupied and returns it.'''
        for i in range(len(self.frames)):
            if self.frames[i] == False:
                self.frames[i] = True
                return i


    def readBlock(self,b,m):
        '''Copies block D[b] into PM frame starting at location PM[m]. Updates ST entry'''

        block = self.disk[b]

        for i in range(len(block)):         #   Read block to physical memory
            self.PM[m+i] = block[i] 

    
    def printPM(self):
        log("Physical memory \n --------------")
        for i in range(len(self.PM)):
            if self.PM[i] != 0:
                print(str(i) + "  |" + str(self.PM[i]) + "| \n")

    def printDisk(self):
        log("Disk \n ---------------")

        for b in range(sizes.BLOCK_QTY):
            for f in range(sizes.BLOCK_SIZE):
                if self.disk[b][f] != 0:
                    print(str(b) + "  |" + str(self.disk[b][f]) + "| \n")


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