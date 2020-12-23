import Node as n
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class BinaryTree:
    '''Construct a binary tree (each node has two child nodes) of depth d = 12 (or more – if you’re feeling lucky)
    and assign different values to each of the 2d leaf-nodes. Specifically, pick the leaf values to be real numbers
    randomly distributed between 0 and 100 (use the uniform continuous distribution U (0, 100), so don’t restrict
    yourself to integer values!).'''

    def __init__(self, depth=12, root=None):
        'Use a uniform random distribution of real numbers from U(0,100) to fill in at least till depth level of 12'
        self.node_count = 0
        self.leaf_count = 0
        self.depth = depth
        self.dist = np.random.uniform(0, 100, 2**(self.depth))
        self.dist_size = len(self.dist)
        self.root = n.Node('NT')
        print(f"node: {self.node_count} ({self.root.value})")


    def traverse_n_fill(self, node, current_depth=0, node_count=0):
        'recursive depth-first traversal'

        if current_depth < self.depth:
            if node.left is None:
                self.node_count+=1
                if current_depth+1 == self.depth:
                    node.left = n.Node(self.dist[self.leaf_count])
                    self.leaf_count+=1
                else:
                    node.left = n.Node('NT')
                print(f"node: {self.node_count} - ({node.left.value}) - orientation: left :: parent: ({node.value})")
                bt.traverse_n_fill(node.left, current_depth+1)
            if node.right is None:
                self.node_count+=1
                if current_depth+1 == self.depth:
                    node.right = n.Node(self.dist[self.leaf_count])
                    self.leaf_count+=1
                else:
                    node.right = n.Node('NT')
                print(f"node: {self.node_count} - ({node.right.value}) - orientation: right :: parent: ({node.value})")
                bt.traverse_n_fill(node.right, current_depth+1)
        
        return node

bt = BinaryTree(2)
print(bt.dist)
tree = bt.traverse_n_fill(bt.root)
print(tree)