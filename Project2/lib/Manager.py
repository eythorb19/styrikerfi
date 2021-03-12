import constants.sizes as sizes
from settings import log

import collections

class Manager:
    def __init__(self, ST, PT):

        self.PM = [None]*sizes.PMsize    #   Physical memory
        self.disk = [[None]*sizes.PTsize]*sizes.STsize    #   Paging disk

        #   Initialization of PM: Segment table
        for i in range(int(len(ST)/3)):
            ss = ST[3*i]       #    Segment ss
            zs = ST[3*i+1]     #    Size zs of segment ss
            fs = ST[3*i+2]  #    Frame fs where PT of segment ss resides in

            self.PM[2*ss] = zs
            self.PM[2*ss+1] = fs

        #   Initialization of PM: Page table
            for j in range(int(len(PT)/3)):
                pp = PT[3*j+1]     #    Page pp of segment sp
                fp = PT[3*j+2]     #    Frame fp where page pp resides in

                self.PM[fs*sizes.PTsize+pp] = fp

    def virtualAddressTranslation(self, VA):
        s = self.bitwiseRightShift(VA, 18)
        w = self.bitwiseMask(self.bitwiseRightShift(VA,9),0xFF)
        p = self.bitwiseMask(VA,0xFF)
        pw = self.bitwiseMask(VA,0xFFF)

        log("s: " + str(s) + " w: " + str(w) + " p: " + str(p) + " pw: " + str(pw))


    def bitwiseRightShift(self,integer,shift):
        '''Bitwise right shift of integer, treated as a binary number.
        Shift defines size of shift.'''
        return integer>>shift
    
    def bitwiseMask(self,integer,mask):
        '''Binary mask.'''
        return integer&mask

    




        



        

