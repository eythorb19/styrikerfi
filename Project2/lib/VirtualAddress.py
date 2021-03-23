class VirtualAddress:
    '''Splits virtual address into s,p,w and pw'''

    def __init__(self, VA):
        self.s = self.bitwiseRightShift(VA, 18)     
        self.p = self.bitwiseMask(self.bitwiseRightShift(VA,9),0x1FF)
        self.w = self.bitwiseMask(VA, 0x1FF)
        self.pw = self.bitwiseMask(VA,0x3FFF)

    def bitwiseRightShift(self,integer,shift):
        '''Bitwise right shift.'''
        return integer>>shift
    
    def bitwiseMask(self,integer,mask):
        '''Binary mask.'''
        return integer&mask
