from BinaryTree import BinaryTree

class Main:
    'Main class for MCTS'

depth = 4

# initialize tree
bt = BinaryTree(depth)

root_node = bt.init_tree(bt.root)
# print distributions
bt.dist.sort()

# mcts
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)
root_node = bt.mcts(root_node)

print(bt.dist)

print(root_node)

# print leaf nodes
for n in bt.leaf_nodes:
    print(f"({n.id}) reward: {n.reward} - ucb: {n.ucb_value}")