from collections import deque
def is_clear(state,block):
    for b, position in state:
        if position in state:
            return False
        return True
def generate_moves(state):
    pass