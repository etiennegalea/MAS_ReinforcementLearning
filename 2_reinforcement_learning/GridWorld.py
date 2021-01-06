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
        self.grid = [[State([j,i]) for i in range(dim)] for j in range(dim)]
        self.init_grid(entities)
        self.total_reward = 0
        self.print = False

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
                self.grid[row][col] = State([row,col], reward, movable, absorbing)

    def print_grid(self, agent_pos, to_show='reward'):
        'Print grid world with rewards in place of state cells'

        print("\n")
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                cell = self.grid[i][j]
                if agent_pos != (i,j):
                    print(f"{cell.print_cell(to_show)}", end="\t")
                else:
                    print(f"{cell.print_cell(to_show, agent_present=True)}", end="\t")
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
                if self.print:
                    print(f"!! Path is blocked (border) !!")
                allowed = False
            elif not self.grid[new_pos[0]][new_pos[1]].movable:
                if self.print:
                    print(f"!! Path is blocked (wall) !!")
                allowed = False
            return allowed

        # perform move
        new_pos = self.move(direction, current_pos)

        # set default state and reward
        pos = current_pos
        reward = 0

        # if the next position is not allowed (in walls or over borders)
        if check_next_pos(current_pos, new_pos):
            if self.print:
                print(f"next position is allowed!")
            reward = self.grid[new_pos[0]][new_pos[1]].reward
            pos = new_pos
            self.total_reward += reward
        # else if it is allowed, incur rewards and new state
        else:
            if self.print:
                print(f"next position is NOT allowed!")
            self.total_reward += -1
            pos = current_pos

        if self.print:
            self.print_grid(pos)
            print(f"{current_pos} --> {pos}")

        return pos        

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
        if self.print:
            print(f"Moved {direction} to: {new_pos}")

        return new_pos
    
    def montecarlo_rl(self, iterations):
        '''
        Calculate V_pi using monte carlo sampling.
        model-free reinforcement learning (RL): finding optimal policies without an explicit model for the MDP
        - complete sample returns for episodic tasks
        - compute value functions using direct sampling (instead of bellman equations)
        - converges asymptotically
        '''

        # repeat for number of iterations
        for iteration in range(iterations):
            print(f"ITERATION: {iteration}")
            for row in range(self.dim):
                for col in range(self.dim):
                    cell = self.grid[row][col]
                    # starting state
                    s = cell
                    pos = s.pos
                    self.total_reward = 0

                    # if the cell in non movable
                    if not self.check_cur_pos(s.pos):
                        cell.v_pi = 0
                        continue

                    while not s.absorbing:
                        # monitoring
                        # sleep(0.1)
                        if self.print:
                            self.clear()

                        pos = self.move_agent(direction=self.random_move_agent(), current_pos=pos)
                        s = self.grid[pos[0]][pos[1]]

                    if self.print:
                        print(f"Terminal state reached: {s.pos} ({s.reward})")
                    cell.v_pi.append(self.total_reward)
                    if self.print:
                        print(f"{cell.pos} v_pi: {cell.v_pi}")
        
        # print results
        for row in range(self.dim):
            print()
            for col in range(self.dim):
                cell = self.grid[row][col]
                cell.v_pi_mean = round(np.mean(cell.v_pi), 2)
                print(f"{cell.pos} :: {cell.v_pi_mean}", end='\t')
                
            cell.v_pi_mean 

    # def init_q_matrix(self):
    #     q_matrix = []
    #     for s in states

    def sarsa(self, episodes=10000, lr=0.1, discount=1, epsilon=0.3, epsilon_decay=0.01):
        'SARSA in combination with greedification to search for an optimal policy'

        def next_action_state(s, a):
            # next state determined by greedy policy (e-greedy)
            new_pos = self.move_agent(a, s.pos)
            s_prime = self.grid[new_pos[0]][new_pos[1]]

            return s_prime, s_prime.reward
            
        actions_per_episode = []
        rewards_per_episode = []
        
        # for each episode
        for ep in range(0, episodes):
            # define starting state
            s = self.grid[0][0]

            # choose action based on policy (e-greedy)
            a = self.e_greedy(s, epsilon)

            # incremently decrease learning-rate per episode until threshold (0.1) is reached
            if epsilon > 0.1:
                epsilon -= epsilon_decay

            actions = 0
            rewards = 0

            # for each step in episode (until done?)
            while True:
                s_prime, reward = next_action_state(s, a)
                a_prime = self.e_greedy(s_prime, epsilon)

                # update algorithm
                s.q[a] = s.q[a] + lr*(reward + discount*(s_prime.q[a_prime]) - s.q[a])

                s = s_prime
                a = a_prime

                actions += 1
                rewards += reward
                
                # repeat until reaching a terminal state
                if s.absorbing:
                    break

            actions_per_episode.append(actions)
            rewards_per_episode.append(rewards)

        # print current gridworld
        self.print_grid(s.pos, to_show='q')
    
        return actions_per_episode, rewards_per_episode

    # def sarsa(self, s, alpha=0.1, discount=1):
    #     'SARSA in combination with greedification to search for an optimal policy'


    def e_greedy(self, s, epsilon=0.1):
        'epsilon-greedy policy returning either random or greedy, depending on rate'

        # if random float is smaller than epsilon, greedy (0 < e < 1)
        if random.random() < epsilon:
            return max(s.q, key=lambda k: s.q[k])
        else:
            # use random policy
            return self.random_move_agent()

    def check_cur_pos(self, current_pos):
        'check if current position allows the agent to be present (possible border or wall)'
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
                    reward += self.move_agent(direction, pos=[i,j])
                reward_matrix[i][j] = reward

        return reward_matrix

    def clear(self):
        # check and make call for specific operating system 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 