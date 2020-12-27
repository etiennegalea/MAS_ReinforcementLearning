from BinaryTree import BinaryTree
from Analytics import Analytics

class Main:
    'Main class for MCTS'

depth = 12
c_values = [0, 0.01, 0.05, 0.1, 0.5, 1, 2, 5]
repeats = 1

statistics = {}

for c in c_values:
    max_rank = 0
    avg_rank = 0
    min_rank = 100
    statistics[c] = {}

    for i in range(0, repeats):
        # initialize tree
        bt = BinaryTree(depth, c)
        root_node = bt.init_tree(bt.root)
        # print distributions
        bt.dist.sort()

        # mcts
        root_node = bt.mcts(root_node)

        # print(bt.dist)
        # print(root_node)

        # print leaf nodes
        # for n in bt.leaf_nodes:
            # print(f"({n.id}) reward: {n.reward} - ucb: {n.ucb_value}")

        stats = Analytics(root_node, bt)
        stats.distribution_stats()
        rank_percent = stats.leaf_node_stats()

        statistics[c][i] = rank_percent

        if max_rank < rank_percent:
            max_rank = rank_percent
        if min_rank > rank_percent:
            min_rank = rank_percent

        avg_rank += rank_percent

    statistics[c]['max'] = max_rank
    statistics[c]['min'] = min_rank
    statistics[c]['avg'] = avg_rank/repeats+1

print(statistics)

stats.create_plots(statistics)