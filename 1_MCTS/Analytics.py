import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Analytics:
    'Analytics for MCTS algorithm'

    def __init__(self, root_node, bt):
        self.root = root_node
        self.dist = bt.dist
        self.leaf_nodes = bt.leaf_nodes
        self.mcts_result = bt.mcts_result

    def distribution_stats(self, c):
        l = len(self.dist)
        percent = int(l*0.05)
        
        # print(f"Length of distribution: {l}")
        # print(f"\nDistribution top 10%:\n{self.dist[-percent:l]}")
        # print(f"\nDistribution bottom 10%:\n{self.dist[0:percent]}")

        # plot distribution
        plt.figure()
        sns.distplot(self.dist)
        plt.xlim(0,100)
        plt.ylabel('Density')
        plt.savefig('./1_MCTS/figs/dist_plot_'+str(c)+'.png')
        plt.show()
        plt.close()

        return

    def leaf_node_stats(self):
        l = len(self.leaf_nodes)
        best_node = self.leaf_nodes[0]
        worst_node = self.leaf_nodes[0]
        rank_result_node =  0

        # get max and min nodes
        for n in self.leaf_nodes:
            if best_node.reward < n.reward:
                best_node = n
            if worst_node.reward > n.reward:
                worst_node = n

        # rank result node
        leaves = self.leaf_nodes
        leaves = sorted(leaves, key=lambda x: x.reward)

        for i in range(0, l):
            if self.mcts_result.reward == leaves[i].reward:
                rank_result_node = i+1

        rank_percent = round((rank_result_node / l)*100, 2)

        # print(f"\nRank of result node: {rank_result_node}/{l} ({rank_percent}%) (reward of {self.mcts_result.reward})")
        # print(f"max reward: {best_node.reward}")
        # print(f"min reward: {worst_node.reward}")

        return rank_percent

    # TODO: violin/box plots
    def create_barplot(self, stats):

        df = pd.DataFrame()
        for c in stats:
            df = df.append({'c': c, 'max': stats[c]['max'], 'min': stats[c]['min'], 'avg': stats[c]['avg']}, ignore_index=True)

        df_melted = df.melt(id_vars='c')

        plt.figure(figsize=(16,10))
        sns.barplot(x='c', y='value', hue='variable', data=df_melted)

        plt.ylim(0, 100)
        plt.ylabel('Reward')
        plt.xlabel('UCB c value')
        plt.legend()

        plt.savefig('./1_MCTS/figs/c_plot.png')
        plt.show()

    def create_boxplot(self, stats, repeats):
        'Box plot for mcts best nodes for different values of c'

        df = pd.DataFrame(stats)
        df = df[0:repeats]

        c_values = [i for i in stats]
        values = [[v for k,v in stats[i].items()] for i in stats]

        plt.figure(figsize=(16,10))
        sns.boxplot(x=c_values, y=values, palette="mako")

        plt.ylabel('Reward')
        plt.xlabel('UCB c value')
        plt.legend()

        plt.savefig('./1_MCTS/figs/c_plot.png')
        plt.show()

