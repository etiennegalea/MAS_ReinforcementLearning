from State import State
import numpy as np

class ReinforcementLearning:

    def __init__(self, agent, entities, dim=9):
        self.agent = agent
        self.dim = dim
        # init grid with empty space (movable and non-absorbing with reward -1)
        self.grid = [[State((i,j)) for i in range(dim)] for j in range(dim)]
        self.init_grid(entities)
        self.total_reward = 0

    def init_grid(self, entities):
        'populate grid world with entities'
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
                row=pos[0]; col=pos[1]
                self.grid[row][col] = State((row,col), reward, movable, absorbing)

    def print_grid(self):
        'Print grid world with rewards in place of state cells'
        print("\n")
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                cell = self.grid[i][j]
                # switch agent pos (for some reason..)
                agent_pos = (self.agent.pos[1], self.agent.pos[0])
                print(f"{cell.print_cell(agent_pos)}", end="\t")
            print("\n")
        
        # print agent position
        print(f":: Agent pos: {self.agent.pos} | Total rewards accumulated: {self.total_reward} ::")
        

    def move_agent(self, direction):
        'move the agent across the grid world'
        current_pos = self.agent.pos
        new_pos = self.agent.move(direction)
        # cell = self.grid[new_pos[0]][new_pos[1]]

        # check if the new position is allowed (wall/border)
        if (new_pos[0] < 0 or new_pos[1] < 0)  or (new_pos[0] > self.dim or new_pos[1] > self.dim):
            print(f"!! Path is blocked (border) !!")
            new_pos = current_pos
            self.total_reward -= 1
        elif not self.grid[new_pos[0]][new_pos[1]].movable:
            print(f"!! Path is blocked (wall) !!")
            new_pos = current_pos
            self.total_reward += self.grid[new_pos[0]][new_pos[1]].reward
        # movement is allowed
        else:
            # incur rewards
            self.total_reward += self.grid[new_pos[0]][new_pos[1]].reward
        self.agent.pos = new_pos

        self.print_grid()

        # check whether agent moved unto an absorbing state
        if self.grid[new_pos[0]][new_pos[1]].absorbing:
            print(f"---------------------- GAME OVER ----------------------")
            # TODO: end_game()
        
        
    # TODO: 
    def calc_state_value(self):
        'calculate the state-value function for the equiprobable policy (1/4) for all 4 actions'

