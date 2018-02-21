
from game import *

class Tens(ReversibleGame):

    @staticmethod
    def initial_state():
        return 10

    @staticmethod
    def final_states():
        return (0,)

    @staticmethod
    def primitive(state):
        if state == 0:
            return Game.LOSE
        return Game.UNDETERMINED

    @staticmethod
    def transitions(state):
        if state == 0:
            return ()
        if state == 1:
            return (1,)
        return (1, 2)

    @staticmethod
    def next(state, transition):
        return state - transition

    @staticmethod
    def reversed_transitions(state):
        if state == 10:
            return ()
        if state == 9:
            return (-1,)
        return (-1, -2)

    @staticmethod
    def reverse(state, reversed_transition):
        return state - reversed_transition
