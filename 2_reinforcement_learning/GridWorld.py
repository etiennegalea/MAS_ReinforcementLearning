from State import State
import numpy as np

class GridWorld:

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
        

    def move_agent(self, direction, pos):
        'move the agent across the grid world'
        
        def check_cur_pos(current_pos):
            'check if current position allows agent'
            allowed = True
            cell = self.grid[current_pos[0]][current_pos[1]]
            if cell.absorbing or not cell.movable:
                allowed = False
            return allowed

        def check_next_pos(current_pos, new_pos):
            '''
            check if the next position is allowed
            if not, leave state unchanged, but still incur rewards
            '''
            reward = 0
            allowed = True
            # check if the new position is allowed (wall/border)
            if (new_pos[0] < 0 or new_pos[1] < 0)  or (new_pos[0] >= self.dim or new_pos[1] >= self.dim):
                print(f"!! Path is blocked (border) !!")
                allowed = False
            elif not self.grid[new_pos[0]][new_pos[1]].movable:
                print(f"!! Path is blocked (wall) !!")
                allowed = False
            return allowed

        # if pos is not defined, assume current agent position
        current_pos = self.agent.pos
        if pos is not None:
            current_pos = pos

        new_pos = self.agent.move(direction, current_pos)

        if not check_cur_pos(current_pos):
            print(f"position {current_pos} is not allowed... skip!")
            return 0
        # elif check_next_pos(current_pos, new_pos):
        if check_next_pos(current_pos, new_pos):
            print(f"next position is allowed!")
            self.print_grid()
            return self.grid[new_pos[0]][new_pos[1]].reward
        else:
            print(f"next position is NOT allowed!")
            return -1


        # self.agent.pos = new_pos


        # check whether agent moved unto an absorbing state
        # if self.grid[new_pos[0]][new_pos[1]].absorbing:
            # print(f"---------------------- GAME OVER ----------------------")
            # TODO: end_game()
        
        # return 
        