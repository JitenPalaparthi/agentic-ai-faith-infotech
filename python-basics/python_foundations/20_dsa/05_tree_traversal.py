class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)

tree = Node(2, Node(1), Node(3))
print(list(inorder(tree)))
