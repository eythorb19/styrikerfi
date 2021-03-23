import constants.sizes as sizes
from settings import log
from lib.VirtualAddress import VirtualAddress
import collections

class Manager:
    def __init__(self, ST, PT):

        self.PM = [None]*(sizes.FRAME_SIZE*sizes.SEGMENT_SIZE)      #   Physical memory
        self.disk = [[None]*sizes.FRAME_SIZE]*sizes.SEGMENT_SIZE    #   Paging disk

        #   Initialization of PM: Segment table
        for i in range(int(len(ST)/3)):
            ss = ST[3*i]       #    Segment ss
            zs = ST[3*i+1]     #    Size zs of segment ss
            fs = ST[3*i+2]     #    Frame fs where PT of segment ss resides in

            self.PM[2*ss] = zs  
            self.PM[2*ss+1] = fs

        #   Initialization of PM: Page table
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

        if va.pw >= self.PM[2*va.s]:
            log("Error: VA is outside of the segment boundary")
            return -1

        else: 
            pageTableIndex = self.PM[2*va.s+1]*sizes.FRAME_SIZE + va.p
            log("Page table index is: " + str(pageTableIndex))
            PA = self.PM[pageTableIndex] * sizes.FRAME_SIZE + va.w
            log("Physical address is: " + str(PA))
            return PA

        return returnVal        


    def printValues(self, segmentNo, pageFrame):
        '''Print value of segment'''
        index = 2*segmentNo
        log("Segment " + str(segmentNo) + " contains value: " + str(self.PM[index]) + " +1: " + str(self.PM[index+1]))
        log("It´s PT " + str(self.PM[self.PM[index+1]*sizes.FRAME_SIZE+pageFrame]))




  

        # Demand paging
        #   Búum til annað array eða vector. 
        #   Á að representa eins og það sé veirð að sækja gögn af disk/skrá.
        #   2D integer array D[B][512] hversu mikið á að sækja