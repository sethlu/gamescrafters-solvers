
# Should be able to work with loopy games

from game import *


def solve(game):

    state_props = {}
    frontier = set()
    for state in game.final_states():
        state_props[state] = {
            'num_children': 0,
            'active_children': set(),
            'val': Game.LOSE,
        }
        frontier.add(state)

    initial_discover = True
    while frontier:

        while frontier:
            print('sizeof frontier: %d, sizeof states: %d' % \
                (len(frontier), len(state_props)))

            state = frontier.pop()
            props = state_props[state]
            for rt in game.reversed_transitions(state):
                parent_state = game.reverse(state, rt)

                if initial_discover:
                    if parent_state not in state_props:
                        state_props[parent_state] = {
                            'num_children': 0,
                            'active_children': set(),
                            'val': Game.UNDETERMINED,
                        }
                        frontier.add(parent_state)
                    state_props[parent_state]['num_children'] += 1
                    state_props[parent_state]['active_children'].add(state)

                parent_props = state_props[parent_state]
                if props['val'] == Game.WIN:
                    parent_props['active_children'].discard(state)
                elif props['val'] == Game.LOSE:
                    parent_props['val'] = Game.WIN
                    frontier.add(parent_state)

        initial_discover = False

        for state, props in state_props.items():
            if len(props['active_children']) == 0:
                if props['val'] == Game.UNDETERMINED:
                    props['val'] = Game.LOSE
                    frontier.add(state)

    return {_[0]: _[1]['val'] for _ in state_props.items()}

# Demo
if __name__ == '__main__':

    # from game_tens import Tens
    # game = Tens

    from game_sticks import Sticks
    game = Sticks()

    for _ in solve(game).items():
        print('%s\t%s' % (game.describe(_[0]), _[1]))
