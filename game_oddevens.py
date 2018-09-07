
from game import *

class OddEvens(Game):

    EVEN = 'EVEN'
    ODD = 'ODD'

    @staticmethod
    def initial_state():
        return (15, OddEvens.EVEN, OddEvens.EVEN)

    @staticmethod
    def primitive(state):
        if state[0] == 0:
            return Game.LOSE
        return Game.UNDETERMINED

    @staticmethod
    def transitions(state):
        return tuple(range(1, min(3, state[0]) + 1))

    @staticmethod
    def next(state, transition):
        if transition % 2:
            # Making an odd move
            return (state[0] - transition, state[2], OddEvens.EVEN if state[1] is OddEvens.ODD else OddEvens.ODD)
        # Making an even move
        return (state[0] - transition, state[2], state[1])
