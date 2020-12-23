class Node:
    'Node class for a binary search tree'
    node_count = 0

    def __init__(self, value=None, depth=0, left=None, right=None):
        self.id = Node.node_count
        self.value = value
        self.node_visits = 0
        self.depth = depth
        self.left = left
        self.right = right
        Node.node_count += 1
    
    def __str__(self):
        return f"({self.value})"
    
# n = Node(5, Node(2), Node(3, 0, Node(20)))
# print(n.left.value)
# print(n.right.right)
# print(Node.node_count)