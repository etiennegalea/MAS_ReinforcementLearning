class RL:
    ''

    def __init__(self, gridworld, dim=9):
        self.dim = dim
        self.gw = gridworld

    # TODO:
    def montecarlo_rl(self, states):
        '''
        model-free reinforcement learning (RL): finding optimal policies without an explicit model for the MDP
        - complete sample returns for episodic tasks
        - compute value functions using direct sampling (instead of bellman equations)
        - converges asymptotically
        '''
        
        # print rewards
        for i in range(0, len(states)):
            for j in range(0, len(states)):
                print(states[i][j].v_pi, end='\t')
            print()

        return


    def calc_rewards(self, agent, policy=0.25):
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
                    reward += self.gw.move_agent(direction, pos=(i,j))
                reward_matrix[i][j] = reward

        return reward_matrix

    # TODO: 
    def calc_state_value(self, policy=0.25):
        'calculate the state-value function for the equiprobable policy (1/4) for all 4 actions'



