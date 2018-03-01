
# coding=utf-8

from game import *
from bidirectionalsolver import solve

def play(game, display_next_val=False):
    sol = {}
    if display_next_val: sol = solve(game)

    state = game.initial_state()
    while game.primitive(state) is Game.UNDETERMINED:
        ts = game.transitions(state)
        ts_str = [str(t) for t in ts]

        print('-' * 10 + '\n%s\nPossible transitions: %s' % (
            game.describe(state),
            '  '.join(unicode(t) +
                (u' → ' + sol[game.next(state, t)] if display_next_val else '')
                for t in ts)))

        print('Enter a transition:')
        t_str = raw_input()
        while t_str not in ts_str:
            print('Re-enter a transition:')
            t_str = raw_input()

        state = game.next(state, ts[ts_str.index(t_str)])

    print(game.primitive(state))

# Demo
if __name__ == '__main__':

    from game_sticks import Sticks
    game = Sticks(
        opt_pass=False,
        opt_wrap=True,
        opt_split_odd=False,
        opt_split_even=False)

    # from game_tens import Tens
    # game = Tens()

    play(game)
