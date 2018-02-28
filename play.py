
from game import *


def play(game):
    state = game.initial_state()
    while game.primitive(state) is Game.UNDETERMINED:
        ts = game.transitions(state)
        ts_str = [str(t) for t in ts]
        print('-' * 10 + '\n%s\nPossible transitions: %s' % (
            game.describe(state),
            '  '.join(unicode(t) for t in ts)))
        print('Enter a transition:')
        t_str = raw_input()
        while t_str not in ts_str:
            print('Re-enter a transition:')
            t_str = raw_input()
        state = game.next(state, ts[ts_str.index(t_str)])
    print(game.primitive(state))


from game_sticks import Sticks
game = Sticks()

# from game_tens import Tens
# game = Tens()

play(game)
