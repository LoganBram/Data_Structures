class Node:
    def __init__(self, key, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
        self.key = key


class BST(Node):

    def __init__(self):
        self.root = None

    # used class slides code to help with this
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.val += value
        return node

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(node.key, node.val)
            self._print_tree(node.right)


b = BST()
b.insert(3, 10)
b.insert(5, 20)
b.insert(8, 30)
b.insert(2, 40)
b.insert(3, 10)

b.print_tree()
