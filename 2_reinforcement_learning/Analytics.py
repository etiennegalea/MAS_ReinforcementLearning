import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Analytics:
    def __init__(self, states):
        self.states = states
    
    def show_heatmap(self):
        'Plot a heatmap of the state values obtained via the Monte Carlo policy evaluation'

        # convert to numpy array
        arr = np.array(self.states)
        arr_v = [[arr[j,i].v_pi_mean for i in range(9)] for j in range(9)]
        # plot heatmap
        plt.rcParams['font.size'] = 6
        sns.heatmap(arr_v, annot=True, fmt='.1f')
        plt.savefig('./2_reinforcement_learning/figs/heatmap.png')
        plt.show()

        print('Done')

    def sarsa_lineplot(self, actions):
        'Show line plot with actions per step'

        index_actions = [i for i in range(len(actions))]

        sns.lineplot(x=index_actions, y=actions)
        plt.savefig('./2_reinforcement_learning/figs/sarsa_actions_per_step.png')
        plt.show()