import Node as n
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

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
        self.root = n.Node(0)
        print(f"node: {self.node_count} ({self.root.value})")


    def init_tree(self, node, current_depth=0, node_count=0):
        'recursive depth-first traversal'

        if current_depth < self.depth:
            if node.left is None:
                self.node_count+=1
                if current_depth+1 == self.depth:
                    node.left = n.Node(self.dist[self.leaf_count])
                    self.leaf_count+=1
                else:
                    node.left = n.Node(0)
                print(f"node: {self.node_count} - ({node.left.value}) - orientation: left :: parent: ({node.id})")
                self.init_tree(node.left, current_depth+1)
            if node.right is None:
                self.node_count+=1
                if current_depth+1 == self.depth:
                    node.right = n.Node(self.dist[self.leaf_count])
                    self.leaf_count+=1
                else:
                    node.right = n.Node(0)
                print(f"node: {self.node_count} - ({node.right.value}) - orientation: right :: parent: ({node.id})")
                self.init_tree(node.right, current_depth+1)
        
        return node

    def mcts(self):
        'Implements the MCTS algorithm and apply it to the tree to search for the optimal (i.e. highest) value'

        
    def mcts_selection(self, root):
        '''
        Use tree-policy to construct path from root to snowcap;
        tree-policy: x_i + c sqrt(log(N)/n_i)
        x_i: mean node value
        n_i: visits of node i
        N: visits of parent
        '''
        return

    def calc_UCBs(self, node):
        return node

    def traverse_snowcap(self, node):
        'traverse till the end of snowcap'

        # if both are unexplored, random choice (rollout)
        if node.left.value == 0 and node.right.value == 0:
            node = self.random_traversal(node)
        else:
            # if left node has a bigger reward than right node
            if node.left.value > node.right.value:
                node = self.traverse_snowcap(node.left)
            else:
                node = self.traverse_snowcap(node.right)

        return node

    def random_traversal(self, node, i=0):
        'choose randomly between going left or right until a leaf-node has been reached'
        if node.value == 0 or i == 0:
            if random.random() < 0.5:
                node = self.random_traversal(node.left, i+1)
            else:
                node = self.random_traversal(node.right, i+1)
        return node


    def mcts_expansion(self):
        'Randomly pick unexplored child'
        
        return


    def mcts_simulation(self):
        'roll-out: random or fast-heuristic'
        
        return


    def mcts_backup(self):
        '''
        Updates values along tree traversal path
        - increments node_visits by while going back up to root (or new root)
        '''
        
        return