
from game import *
from itertools import product, permutations

class Sticks(ReversibleGame):

    @staticmethod
    def final_states(): # Some may not be possible to reach
        return [state for state in product(product([1, 2, 3, 4, 5], repeat=2), repeat=2)
            if state[0][0] == 5 or state[0][1] == 5 or state[1][0] == 5 or state[1][1] == 5]

    @staticmethod
    def primitive(state):
        if state[0][0] == 5 and state[0][1] == 5:
            return Game.LOSE
        if state[1][0] == 5 and state[1][1] == 5:
            return Game.WIN
        return Game.UNDETERMINED

    @staticmethod
    def reversed_transitions(state):
        rts = []
        if state[0][0] - state[1][0] > 0:
            rts.append('ll')
        if state[0][0] - state[1][1] > 0:
            rts.append('rl')
        if state[0][1] - state[1][0] > 0:
            rts.append('lr')
        if state[0][1] - state[1][1] > 0:
            rts.append('rr')
        if state[1][0] == state[1][1] == 2:
            rts.append('04-22')
            rts.append('40-22')
        return rts

    @staticmethod
    def reverse(state, reversed_transition):
        if reversed_transition == 'll':
            return ((state[1][0], state[1][1]),
                    (state[0][0] - state[1][0], state[0][1]))
        elif reversed_transition == 'lr':
            return ((state[1][0], state[1][1]),
                    (state[0][0], state[0][1] - state[1][0]))
        elif reversed_transition == 'rl':
            return ((state[1][0], state[1][1]),
                    (state[0][0] - state[1][1], state[0][1]))
        elif reversed_transition == 'rr':
            return ((state[1][0], state[1][1]),
                    (state[0][0], state[0][1] - state[1][1]))
        elif reversed_transition == '04-22':
            return ((0, 4),
                    (state[0][0], state[0][1]))
        elif reversed_transition == '40-22':
            return ((4, 0),
                    (state[0][0], state[0][1]))

    @staticmethod
    def describe(state):
        return 'me %d %d & other %d %d' % \
            (state[0][0], state[0][1], state[1][0], state[1][1])
