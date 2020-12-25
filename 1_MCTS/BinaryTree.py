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
        self.c = 2
        self.leaf_nodes = []
        print(f"node: {self.node_count} ({self.root.reward})")


    def init_tree(self, node, current_depth=0, node_count=0):
        'recursive depth-first traversal'

        if current_depth < self.depth:
            if node.left is None:
                # self.node_count+=1
                if current_depth+1 == self.depth:
                    node.left = n.Node(self.dist[self.leaf_count])
                    self.leaf_count+=1
                    self.leaf_nodes.append(node)
                else:
                    node.left = n.Node(0)
                # print(f"node: {self.node_count} - ({node.left.reward}) - orientation: left :: parent: ({node.id})")
                self.init_tree(node.left, current_depth+1)
            if node.right is None:
                # self.node_count+=1
                if current_depth+1 == self.depth:
                    node.right = n.Node(self.dist[self.leaf_count])
                    self.leaf_count+=1
                    self.leaf_nodes.append(node)
                else:
                    node.right = n.Node(0)
                # print(f"node: {self.node_count} - ({node.right.reward}) - orientation: right :: parent: ({node.id})")
                self.init_tree(node.right, current_depth+1)
        
        return node

    def mcts(self, root):
        'Implements the MCTS algorithm and apply it to the tree to search for the optimal (i.e. highest) value'
        best_reward_node = self.selection(root)

        return best_reward_node

        
    def selection(self, root):
        result = root
        while result is not None:
            result = self.traverse_snowcap(result)

        return result

    def traverse_snowcap(self, node, parent_node=None, expanded=False):
        'traverse till the end of snowcap'

        node.visits += 1

        if not expanded:
            if node.left.ucb_value > node.right.ucb_value:
                self.traverse_snowcap(node.left, node)
            elif node.left.ucb_value < node.right.ucb_value:
                self.traverse_snowcap(node.right, node)
            # if both are unexplored (or equal), random choice (rollout)
            elif node.left.ucb_value == node.right.ucb_value:
                self.traverse_snowcap(self.expansion(node), node, expanded=True)

        # check if leaf node
        if node.left is None and node.right is None:
            print(f"BEST REWARD ---> {node.reward} <---")
            return None

        leaf_reward = self.simulation(node)
        node = self.backup(node, parent_node, leaf_reward)


        return node

    def expansion(self, node):
        'Randomly pick unexplored child'
        if random.random() < 0.5:
            return node.left
        else:
            return node.right


    def calc_UCB(self, node, parent_visits):
        '''
        Use tree-policy to construct path from root to snowcap;
        tree-policy: x_i + c sqrt(log(N)/n_i)
        x_i: mean node value
        n_i: visits of node i
        N: visits of parent
        '''
        n = node.visits
        N = parent_visits
        x = node.reward / n
        c = self.c
        
        node.ucb_value = x + c*(np.sqrt(np.log(N)/n))
        return node

    def simulation(self, node):
        'roll-out: random or fast-heuristic'
        while node.left is not None or node.right is not None:
            if random.random() < 0.5:
                node = node.left
            else:
                node = node.right
        return node.reward


    def backup(self, node, parent_node, leaf_reward):
        'Updates values along tree traversal path (reward and visits)'
        if node.left is not None or node.right is not None:
            node.reward += leaf_reward

        # root node has no parent and therefore no UCB
        if parent_node is None:
            return node
            
        # calculate UCB for children nodes
        node = self.calc_UCB(node, parent_node.visits)
        return node


    def is_terminal(self, node):
        'Returs true if node is terminal (has no children)'
        if node.left is None and node.right is None:
            return True
        else:
            return False