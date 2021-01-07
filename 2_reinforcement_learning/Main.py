from Agent import Agent
from GridWorld import GridWorld
import copy
from Analytics import Analytics

class Main:
    'SARSA and Q-learning'


# length and width of gridworld (assuming square grid so length = width)
dim = 9
# where the agent will start from
spawn = [0,0]

# entities in the grid world:
    # walls (blue squares)
    # negative terminal node (red square)
    # positive terminal node (green square)
    # INDICES START AT 0
entities = {
    'blue': [[1,2], [1,3], [1,4], [1,5], [1,6], [2,6], [3,6], [4,6], [5,6], [7,1], [7,2], [7,3], [7,4]],
    'red': [[6,5]],
    'green': [[8,8]]
}

# create agent
agent = Agent(spawn)
# creating grid world
gw = GridWorld(agent, entities, dim)

# Analytics class
stats = Analytics(gw.grid)

# Use Monte Carlo policy evaluation to compute the state value function v_pi(s) for the equiprobable policy pi
# gw.montecarlo_rl(iterations=10000)
# stats.show_heatmap(gw.grid)

# sarsa
actions, rewards = gw.sarsa(episodes=5000)
stats.temp_diff_lineplot(actions, algorithm='sarsa')
stats.temp_diff_lineplot_actions_rewards(actions, rewards, algorithm='sarsa')
# stats.temp_diff_lineplot(rewards, algorithm='sarsa')
# qlearning
actions, rewards = gw.qlearning(episodes=5000)
stats.temp_diff_lineplot(actions, algorithm='qlearning')
stats.temp_diff_lineplot_actions_rewards(actions, rewards, algorithm='qlearning')


# manual control of agent (for testing)
# current_pos = spawn
# while True:
#     x = str(input())
#     if x=='north' or  x=='south' or x=='west' or x=='east':
#         current_pos = gw.move_agent(x, current_pos)
#     else:
#         break
    