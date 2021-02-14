class PCBarray:
    def __init__(self):
        self.A = [None]*8           
        self.capacity = 8
        self.n = 0

    def __len__(self):
        return self.n

    def freeColumn(self):
        '''Find the next free column. Resize the array if it´s too small.'''
        for i in self.capacity:
            if self.PCBn[i] == None:
                return i
            
            #   If it´s full resize the array
            self.resize()
            return self.n+1


    def resize(self):
        self.capacity*=2            #   Double the capacity of the PCBarray
        arr = [None]*self.capacity

        for i in len(self.A):
            arr[i] = self.A[i]
        

        for i