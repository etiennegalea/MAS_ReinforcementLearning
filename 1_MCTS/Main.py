from BinaryTree import BinaryTree
from Analytics import Analytics

class Main:
    'Main class for MCTS'

depth = 12

# initialize tree
bt = BinaryTree(depth)
root_node = bt.init_tree(bt.root)
# print distributions
bt.dist.sort()

# mcts
iter = 0
while not bt.is_terminal(root_node):
    iter += 1
    print(f"ITERATION {iter}")
    for i in range(0, 25):
        root_node = bt.mcts(root_node)

    print(f"left: {root_node.left.ucb_value}")
    print(f"right: {root_node.right.ucb_value}")

    if root_node.left.ucb_value > root_node.right.ucb_value:
        root_node = root_node.left
    else:
        root_node = root_node.right



# print(bt.dist)
# print(root_node)

# print leaf nodes
# for n in bt.leaf_nodes:
    # print(f"({n.id}) reward: {n.reward} - ucb: {n.ucb_value}")

stats = Analytics(root_node, bt)
stats.distribution_stats()
stats.leaf_node_stats()