import numpy as np

class Node:
    'Node class for a binary search tree'
    node_count = 0

    def __init__(self, reward=0, depth=0, left=None, right=None):
        self.id = Node.node_count
        self.reward = reward
        self.ucb_value = np.inf
        self.visits = 0
        self.depth = depth
        self.left = left
        self.right = right
        Node.node_count += 1
    
    def __str__(self):
        return f"({self.reward}) - UCB: {self.ucb_value}"
