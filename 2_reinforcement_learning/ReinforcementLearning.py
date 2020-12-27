from State import State
import numpy as np

class ReinforcementLearning:

    def __init__(self, entities, dim=9):
        # init grid world
        # self.grid = np.empty(shape=(dim,dim), dtype=State()
        self.grid = [[State() for i in range(dim)] for j in range(dim)] 

        # populating grid world
        for ent_type in entities:
            # blue
            reward = -1
            movable = False
            absorbing = False
            # red
            if ent_type == 'red':
                reward = -50
                movable = True
                absorbing = True
            # green
            elif ent_type == 'green':
                reward = 50
                movable = True
                absorbing = True

            # set state for defined positions
            for pos in entities[ent_type]:
                x=pos[0]; y=pos[1]
                self.grid[x][y] = State(reward, movable, absorbing)

    def init_grid(self):
        return None

    def print_grid(self):
        # priting grid world
        for i in range(0, 9):
            for j in range(0, 9):
                print(i,j)