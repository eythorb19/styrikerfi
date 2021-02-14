import constants.priority
import constants.states as STATE
import collections

class RCB:
    state = STATE.FREE
    waitList = collections.deque()    #   Wait list with processes

    def __str__(self):
        return 'Resource with state: {self._state}'.format(self=self)