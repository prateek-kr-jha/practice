class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = Node(left) if left else left
        self.right = Node(right)
