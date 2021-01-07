import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

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

    def temp_diff_lineplot(self, values, algorithm):
        'Show line plot with actions per step'

        indexes = [i for i in range(len(values))]

        sns.lineplot(x=indexes, y=values)

        plt.xlabel('episodes')
        plt.ylabel('actions')

        plt.savefig('./2_reinforcement_learning/figs/'+algorithm+'_actions_per_episode.png')
        plt.show()
        plt.clf()

        print(f"{algorithm}: actions after learning: {values[-1]}")



    def temp_diff_lineplot_actions_rewards(self, actions, rewards, algorithm):
        'Show line plot with actions/rewards per step'

        indexes = [i for i in range(len(actions))]

        # df = pd.DataFrame({'index': indexes, 'actions': actions, 'rewards': rewards})
        # grouped = df.groupby({x: x // 100 for x in range(len(df))})

        sns.lineplot(x=indexes, y=actions)
        sns.lineplot(x=indexes, y=rewards)

        plt.xlabel('episodes')
        plt.legend(['n actions', 'rewards'])

        plt.savefig('./2_reinforcement_learning/figs/'+algorithm+'_actions_rewards_per_episode.png')
        plt.show()
        plt.clf()

        print(f"actions after learning: {actions[-1]}\nMax total reward yield: {rewards[-1]}")


    def compare_algorithms_lineplot(self, sarsa_actions, qlearning_actions, value_type):
        'Show line plot with actions/rewards per step'

        index = [i for i in range(len(max(sarsa_actions, qlearning_actions)))]
        df = pd.DataFrame({'episodes': index, 'sarsa': sarsa_actions, 'qlearning': qlearning_actions})

        _df = df.melt(id_vars='episodes', value_vars=['sarsa', 'qlearning'])
        sns.lineplot(data=_df, x='episodes', y='value', hue='variable')

        plt.xlabel('episodes')
        plt.ylabel('num of actions')
        plt.legend(['SARSA', 'Q-learning'])

        plt.savefig('./2_reinforcement_learning/figs/'+value_type+'_actions_rewards_per_episode.png')
        plt.show()
        plt.clf()

        print(f"SARSA: actions after learning - {sarsa_actions[-1]}")
        print(f"Q-Learning: actions after learning - {qlearning_actions[-1]}")