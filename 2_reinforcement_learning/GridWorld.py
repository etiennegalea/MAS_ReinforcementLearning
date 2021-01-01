from State import State
import numpy as np
import random
import copy
from os import system, name
from time import sleep

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

    def print_grid(self, agent_pos):
        'Print grid world with rewards in place of state cells'

        # agent_pos = self.agent.pos
        # if pos is not None:
        #     agent_pos = pos

        # switch agent pos (for some reason..)
        agent_pos = (agent_pos[1], agent_pos[0])
        print("\n")
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                cell = self.grid[i][j]
                if agent_pos != (j,i):
                    print(f"{cell.print_cell()}", end="\t")
                else:
                    print(f"{cell.print_cell(agent_present=True)}", end="\t")
            print("\n")
        
        # print agent position
        print(f":: Agent pos: {agent_pos} | Total rewards accumulated: {self.total_reward} ::")
        

    def move_agent(self, direction, current_pos):
        'move the agent across the grid world'

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
        # current_pos = self.agent.pos
        # if pos is not None:
            # current_pos = pos

        # perform move
        new_pos = self.move(direction, current_pos)

        # set default state and reward
        # state = self.grid[current_pos[0]][current_pos[1]]
        pos = current_pos
        reward = 0

        # if the current position is impossible (in walls or over borders)
        # if not check_cur_pos(current_pos):
        #     print(f"position {current_pos} is not allowed... skip!")
        #     reward = 0
        # if the next position is not allowed (in walls or over borders)
        if check_next_pos(current_pos, new_pos):
            print(f"next position is allowed!")
            reward = self.grid[new_pos[0]][new_pos[1]].reward
            pos = new_pos
            self.total_reward += reward
            # update agent position
            # if pos is None:
            #     self.agent.pos = state.pos
        # else if it is allowed, incur rewards and new state
        else:
            print(f"next position is NOT allowed!")
            self.total_reward += -1
            pos = current_pos

        self.print_grid(pos)
        print(f"{current_pos} --> {pos}")

        return pos


        # self.agent.pos = new_pos


        # check whether agent moved unto an absorbing state
        # if self.grid[new_pos[0]][new_pos[1]].absorbing:
            # print(f"---------------------- GAME OVER ----------------------")
            # TODO: end_game()
        
        # return 
        

    def random_move_agent(self):
        'Move in a random direction with an equiprobable policy of 1/4'
        r = random.random()
        direction = ''
        if r < 0.25:
            direction = 'north'
        elif r < 0.5:
            direction = 'south'
        elif r < 0.75:
            direction = 'east'
        elif r < 1:
            direction = 'west'

        return direction

    
    def move(self, direction, current_pos):
        'move agent in a direction'

        # if pos is not defined, assume current agent position
        # current_pos = self.agent.pos
        # if pos is not None:
        #     current_pos = pos


        row=0; col=0
        if direction == 'north':
            row = -1
        elif direction == 'south':
            row = 1
        elif direction == 'east':
            col = 1
        elif direction == 'west':
            col = -1
         
        new_pos = (current_pos[0]+row, current_pos[1]+col)
        print(f"Moved {direction} to: {new_pos}")

        return new_pos
    
    
    # TODO:
    def montecarlo_rl(self):
        '''
        Calculate V_pi using monte carlo sampling.
        model-free reinforcement learning (RL): finding optimal policies without an explicit model for the MDP
        - complete sample returns for episodic tasks
        - compute value functions using direct sampling (instead of bellman equations)
        - converges asymptotically
        '''
        
        for row in range(self.dim):
            for col in range(self.dim):
                cell = self.grid[col][row]
                # starting state
                s = cell
                pos = s.pos
                self.total_reward = 0

                # if the cell in non movable
                if not self.check_cur_pos(s.pos):
                    cell.v_pi = 0
                    break

                while not s.absorbing:
                    # monitoring
                    # sleep(0.1)
                    self.clear()

                    pos = self.move_agent(direction=self.random_move_agent(), current_pos=pos)
                    s = self.grid[pos[1]][pos[0]]

                print(f"Terminal state reached: {s.pos} ({s.reward})")
                cell.v_pi = self.total_reward
        
        # print results
        for row in range(self.dim):
            for col in range(self.dim):
                cell = self.grid[col][row]
                print(f"{cell.pos} :: {cell.v_pi}")


    def check_cur_pos(self, current_pos):
        'check if current position allows agent'
        cell = self.grid[current_pos[0]][current_pos[1]]
        if cell.absorbing or not cell.movable:
            return False
        else:
            return True


    def calc_all_rewards(self, agent, policy=0.25):
        'calculate expected immediate reward in state s under the specified policy'
        # init matrix
        reward_matrix = [[0 for i in range(self.dim)] for j in range(self.dim)]
        
        directions = ['north', 'south', 'east', 'west']
    
        # loop over all the states in the matrix
        for i in range(self.dim):
            for j in range(self.dim):
                # calculate expected immediate reward for each state
                reward = 0
                for direction in directions:
                    reward += self.move_agent(direction, pos=(i,j))
                reward_matrix[i][j] = reward

        return reward_matrix

    # TODO: 
    def calc_state_value(self, policy=0.25):
        'calculate the state-value function for the equiprobable policy (1/4) for all 4 actions'



    def clear(self):
        # check and make call for specific operating system 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 