import constants.priority as PRIORITY
import constants.states as STATE
import collections


class PCB:
    #   TODO: Add priority
    def __init__(self, parent, priority):
        self.parent = parent
        self.priority = priority
        self.children = collections.deque()
        self.state = STATE.READY
        self.resources = collections.deque()



    def __str__(self):
        return 'A {self._state} process'.format(self=self)