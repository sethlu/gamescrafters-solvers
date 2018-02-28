
# coding=utf-8

# Should be able to work with loopy games

from game import *


def solve(game):

    state_props = {}
    frontier = set()

    def traverse(state, parent=None):
        if state in state_props:
            # parent should be not be empty
            state_props[state]['parents'].add(parent)
            return
        state_props[state] = {
            'parents': set(),
            'children': set(),
            'active_children': set(),
            'val': game.primitive(state),
        }
        if parent:
            state_props[state]['parents'].add(parent)
        frontier.add(state)
        for t in game.transitions(state):
            next_state = game.next(state, t)

            state_props[state]['children'].add(next_state)
            state_props[state]['active_children'].add(next_state)
            traverse(next_state, state)

    traverse(game.initial_state())

    while frontier:
        state = frontier.pop()
        props = state_props[state]

        if props['val'] == Game.UNDETERMINED \
            and len(props['active_children']) == 0 \
            and len(props['children']) > 0: # Undetermined
            props['val'] = Game.LOSE

        if props['val'] == Game.LOSE:
            for parent in props['parents']:
                if state_props[parent]['val'] == Game.UNDETERMINED:
                    state_props[parent]['val'] = Game.WIN
                    frontier.add(parent) # State changed
        elif props['val'] == Game.WIN:
            for parent in props['parents']:
                if state in state_props[parent]['active_children']:
                    state_props[parent]['active_children'].remove(state)
                    frontier.add(parent) # State changed

    return {_[0]: _[1]['val'] for _ in state_props.items()}

# Demo

# from game_tens import Tens
# game = Tens

from game_sticks import Sticks
game = Sticks(
    opt_pass=True,
    opt_wrap=True,
    opt_split_odd=True,
    opt_split_even=True)

for _ in solve(game).items():
    print('%s\t%-12s\t%s' % (
        game.describe(_[0]), _[1],
        '  '.join(unicode(t) + u' → ' + unicode(game.describe(game.next(_[0], t)))
            for t in game.transitions(_[0]))))
