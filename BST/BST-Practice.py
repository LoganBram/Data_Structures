from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST(Node):

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node == None:
            return Node(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        elif key > node.val:
            node.right = self._insert(node.right, key)
        return node

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node != None:
            self._inorder(node.left)
            print(node.val)
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node != None:
            print(node.val)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node != None:
            self._preorder(node.left)
            self._preorder(node.right)
            print(node.val)

    def levelorder(self):
        self._levelorder(self.root)

    def _levelorder(self, node):
        temp = None
        q = Queue()
        q.put(node)
        while q.empty() is not True:
            temp = q.get()
            print(temp.val)
            if temp.left != None:
                q.put(temp.left)
            if temp.right != None:
                q.put(temp.right)

    def findHeightUtil(self, root, x):
        global height

        # Base Case
        if (root == None):
            return -1

        # Store the maximum height of
        # the left and right subtree
        leftHeight = self.findHeightUtil(root.left, x)

        rightHeight = self.findHeightUtil(root.right, x)

        # Update height of the current node
        ans = max(leftHeight, rightHeight) + 1

        # If current node is the required node
        if (self.root.val == x):
            height = ans

        return ans

    # Function to find the height of
    # a given node in a Binary Tree

    def findHeight(self, x):
        global height

        # Stores height of the Tree
        maxHeight = self.findHeightUtil(self.root, x)

        # Return the height
        print(maxHeight)


bst = BST()

q = Queue()


bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(13)


bst.inorder()
print("")
bst.preorder()
print("")
bst.postorder()
print("")
bst.levelorder()

print("")
bst.findHeight(bst.root)
