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

    def sarsa_lineplot(self, actions, rewards):
        'Show line plot with actions per step'

        indexes = [i for i in range(len(actions))]

        sns.lineplot(x=indexes, y=actions)
        sns.lineplot(x=indexes, y=rewards)

        plt.xlabel('episodes')
        plt.legend(['n actions', 'rewards'])

        plt.savefig('./2_reinforcement_learning/figs/sarsa_actions_rewards_per_episode.png')
        plt.show()