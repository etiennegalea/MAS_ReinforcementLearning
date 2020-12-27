from ReinforcementLearning import ReinforcementLearning as rl
from Agent import Agent

class Main:
    'SARSA and Q-learning'


# length and width of gridworld (assuming square grid so length = width)
dim = 9
# where the agent will start from
spawn = (8,7)

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
gw = rl(agent, entities, dim)
gw.print_grid()

gw.move_agent('right')