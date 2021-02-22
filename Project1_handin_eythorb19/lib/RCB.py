import constants.states as STATE
import collections

class RCB:
    '''Resource that processes can request. Has a state and a waitlist. '''
    def __init__(self):
        self.state = STATE.FREE
        self.waitList = collections.deque()  #   Wait list with processes

    def __str__(self):
        return 'Resource with state: {self.state}'.format(self=self)