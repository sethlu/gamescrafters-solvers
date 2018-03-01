
# Not intended for loopy games

from game import *


def solve(game):

    cache = {}
    def simple_memoized(func):
        def decorated(arg):
            if arg not in cache:
                cache[arg] = func(arg)
            return cache[arg]
        return decorated

    @simple_memoized
    def query(state):
        primitive = game.primitive(state)
        if primitive is not Game.UNDETERMINED:
            return primitive
        if [query(game.next(state, t)) for t in game.transitions(state)] \
            .count(Game.LOSE):
            return Game.WIN
        return Game.LOSE

    query(game.initial_state())
    return cache

# Demo
if __name__ == '__main__':

    from game_tens import Tens
    game = Tens()

    for _ in solve(game).items():
        print('%s\t%s' % (game.describe(_[0]), _[1]))
