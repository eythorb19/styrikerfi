import constants.priority 
import constants.states


class PCB:
    _children = 0
    _resources = 0
    _state = constants.states.READY

    def __init__(self, parent, priority):
        self._parent = parent
        self._priority = priority

    def __str__(self):
        return 'A {self._state} process'.format(self=self)