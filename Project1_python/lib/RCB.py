import constants.priority
import constants.states

class RCB:
    _state = constants.states.FREE
    _waitList = []    #   Wait list with processes

    def __str__(self):
        return 'Resource with state: {self._state}'.format(self=self)