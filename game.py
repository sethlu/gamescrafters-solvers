
class Game:

    WIN = 'WIN'
    LOSE = 'LOSE'
    UNDETERMINED = 'UNDETERMINED'

    @staticmethod
    def initial_state():
        raise NotImplementedError

    @staticmethod
    def primitive(state):
        raise NotImplementedError

    @staticmethod
    def transitions(state):
        raise NotImplementedError

    @staticmethod
    def next(state, transition):
        raise NotImplementedError

    @staticmethod
    def describe(state):
        return state


class ReversibleGame(Game):

    @staticmethod
    def reversed_transitions(state):
        raise NotImplementedError

    @staticmethod
    def reverse(state, reversed_transition):
        raise NotImplementedError

    @staticmethod
    def final_states():
        raise NotImplementedError
