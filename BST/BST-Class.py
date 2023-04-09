from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0


class BST(Node):

    def __init__(self):
        self.root = None

    # used class slides code to help with this
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        elif key > node.val:
            node.right = self._insert(node.right, key)
        # need seperate get height method in case node is None, so error isnt thrown. shown in  delete helper also
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        return node

    def inorder(self):
        self.inorderhelp(self.root)

    def inorderhelp(self, node):
        # class slides helped with this as well sorta
        if node != None:
            self.inorderhelp(node.left)
            print(node.val)
            self.inorderhelp(node.right)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        # traverse based on value
        if value < node.val:
            node.left = self._delete(node.left, value)
        elif value > node.val:
            node.right = self._delete(node.right, value)
        else:
            # deletion once value found
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        return node

    # helper method for deletion
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def save(self):
        list = self.savehelp(self.root, [])
        # turns returned list from savehelp, into a string
        seperate = ','
        string = seperate.join(str(x) for x in list)
        self.restore(string)

    def savehelp(self, curr, list):
        # makes tree into list recursively
        if curr == None:
            return curr
        list.append(curr.val)
        self.savehelp(curr.left, list)
        self.savehelp(curr.right, list)
        return list

    def restore(self, input_string):
        # splits values in string into list via ,
        vals = input_string.split(',')
        # changes strings to ints
        for i in range(len(vals)):
            vals[i] = int(vals[i])
        self.root = None
        # inserts values into tree to restore
        for i in vals:
            self.insert(i)

    # gets height of node
    def _get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def get_total_height(self):
        sum = self.get_total_height_helper(self.root, 0)
        return sum

    def get_total_height_helper(self, node, sum):
        # traverse inorder and return sum
        if node != None:
            self.get_total_height_helper(node.left, sum)
            sum += node.height
            self.get_total_height_helper(node.right, sum)
            sum += node.height
        return sum


# create a new BST instance
bst = BST()

# insert some nodes
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(13)

# total_height = bst.get_total_height()
# print(total_height)

print("after insertion, printing in-order: ")
bst.inorder()

print("sum of tree")
print(bst.get_total_height())


print("tree after deleting two child (5): ")
bst.delete(5)
bst.inorder()

print("tree after deleting one child node(15): ")
bst.delete(15)
bst.inorder()

print("tree after deleting no child node (3):")
bst.delete(3)
bst.inorder()

print("tree after save and restoration, inserted more nodes, restore is ran within save: ")

bst.insert(5)
bst.insert(12)
bst.insert(8)
bst.save()
bst.inorder()

print(" ")
