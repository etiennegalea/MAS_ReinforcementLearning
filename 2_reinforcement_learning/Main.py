from Agent import Agent
from GridWorld import GridWorld
from RL import RL

class Main:
    'SARSA and Q-learning'


# length and width of gridworld (assuming square grid so length = width)
dim = 9
# where the agent will start from
spawn = (0,0)

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
# gw.print_grid()

rl = RL(gw)
print(rl.calc_rewards(agent, policy=0.25))

# manual control of agent (for testing)
# while True:
#     x = str(input())
#     if x=='north' or  x=='south' or x=='west' or x=='east':
#         gw.move_agent(x)
#     else:
#         break
    