from State import State
from Agent import Agent
import numpy as np

class ReinforcementLearning:

    def __init__(self, entities, dim=9):
        # init grid world
        # self.grid = np.empty(shape=(dim,dim), dtype=State()
        self.agent = Agent()
        self.dim = dim
        self.grid = [[State() for i in range(dim)] for j in range(dim)] 
        self.init_grid(entities)

    def init_grid(self, entities):
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


    def print_grid(self):
        'Print grid world with rewards in place of state cells'
        print("\n")
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                x = self.grid[i][j]
                if x.movable:
                    print(f"{self.grid[i][j].reward}", end="\t")
                # if not, it is a wall
                else:
                    print(f"[{self.grid[i][j].reward}]", end="\t")
            print("\n")
        
        # print agent position
        print(self.agent)