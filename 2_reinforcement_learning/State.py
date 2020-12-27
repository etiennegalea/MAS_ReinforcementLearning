class State:
    'Defined state of cell in grid world'
    def __init__(self, reward= -1, movable=True, absorbing=False):
        self.reward = reward
        self.movable = movable
        self.absorbing = absorbing
