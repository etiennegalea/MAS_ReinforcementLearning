import seaborn as sns
import matplotlib.pyplot as plt

class Analytics:
    'Analytics for MCTS algorithm'

    def __init__(self, root_node, bt):
        self.root = root_node
        self.dist = bt.dist
        self.leaf_nodes = bt.leaf_nodes
        self.mcts_result = bt.mcts_result

    def distribution_stats(self):
        l = len(self.dist)
        percent = int(l*0.05)
        
        print(f"Length of distribution: {l}")
        # print(f"\nDistribution top 10%:\n{self.dist[-percent:l]}")
        # print(f"\nDistribution bottom 10%:\n{self.dist[0:percent]}")

        # plot distribution
        sns.distplot(self.dist)
        plt.savefig('dist_plot.png')

        return

    def leaf_node_stats(self):
        l = len(self.dist)
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
        sorted(leaves, key=lambda x: x.reward, reverse=True)

        for i in range(0, l):
            if self.mcts_result.reward == self.leaf_nodes[i].reward:
                rank_result_node = i

        rank_result_node = round((rank_result_node / l), 4) * 100
        print(f"\nRank of result node: {rank_result_node}% (reward of {self.mcts_result.reward})")
