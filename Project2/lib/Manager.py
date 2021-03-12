import constants.sizes as sizes
from settings import log

import collections

class Manager:
    def __init__(self):

        print(sizes.STsize)
        self.PM = [None]*sizes.PMsize    #   Physical memory
        self.disk = [sizes.STsize][sizes.PTsize]    #   Paging disk

        x = [[foo for i in range(10)] for j in range(10)]



    
        


#  •	The VM manager initializes the PM from an input file consisting of 2 lines. 
# •	Line 1 contains triples of integers, which define the contents of the ST
# •	Line 2 contains triples of integers, which define the contents of the PTs
# •	The initialization file is syntactically correct in that:
# •	Line 1 correctly specifies 1 or more segment table entries
# •	Line 2 correctly specifies 0 or more entries in PTs for the segments specified on line 1
