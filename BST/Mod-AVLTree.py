import re
import string
from nltk.corpus import stopwords


class Node:
    def __init__(self, val, frequency=1):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.frequency = frequency


class AVLTreeMap:
    def __init__(self):
        self.root = None
        self.stop_words = set(stopwords.words('english'))

    def fileloader(self, filepath):
        self.root = None
        words = self.parse_file(filepath)
        for word in words:
            self.insert(word)

    def parse_file(self, filepath):
        with open(filepath, 'r') as f:
            textfile = f.readlines()
            words = []
            for line in textfile:
                # textfile is now a string of the text file
                line = line.strip().lower()
                # seperated each line via periods
                line = line.translate(
                    str.maketrans('', '', string.punctuation))
                # eliminated periods
                line = self.remove_stopwords(line)
                # got rid of redudent terms such as the, this, is ETC

                line = re.sub('\d+', '', line)
                line = re.sub(' +', ' ', line)
                # now put into list form
                if line:
                    words.extend(line.split(" "))
            return words

    def remove_stopwords(self, text):
        return " ".join([word for word in str(text).split() if word not in self.stop_words])

    def insert(self, word):
        self.root = self.inserthelp(self.root, word)

    def inserthelp(self, node, word):
        # used combo of slides and internet to help with this
        if node is None:
            return Node(word)
        if word > node.val:
            node.right = self.inserthelp(node.right, word)
        elif word < node.val:
            node.left = self.inserthelp(node.left, word)
        else:
            node.frequency += 1
            return node

        # update height of the current node
        node.height = 1 + max(self.getheight(node.left),
                              self.getheight(node.right))

        # check balance of tree currently
        BalanceValue = self.get_BalanceFactor(node)

        # if balance factor is less than -1 & new word is smaller then nodes right child
        if BalanceValue < -1 and word < node.right.val:
            node.right = self.rotateright(node.right)
            return self.rotateleft(node)

        # if balance greater then 1, same as above but reverse
        if BalanceValue > 1 and word > node.left.val:
            node.left = self.rotateleft(node.left)
            return self.rotateright(node)

        # if balance factor is less than -1, it means the tree is right heavy
        if BalanceValue < -1 and word > node.right.val:
            return self.rotateleft(node)

        # if balance factor is greater than 1, it means the tree is left heavy
        if BalanceValue > 1 and word < node.left.val:
            return self.rotateright(node)

        return node

    def getheight(self, node):
        if node is None:
            return 0
        return node.height

    def get_BalanceFactor(self, node):
        if node is None:
            return 0
        return self.getheight(node.left) - self.getheight(node.right)

    def rotateleft(self, node):
        if node is None or node.right is None:
            return node

        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self.getheight(node.left),
                              self.getheight(node.right))
        new_root.height = 1 + \
            max(self.getheight(new_root.left), self.getheight(new_root.right))

        return new_root

    def rotateright(self, node):
        if node == None or node.left == None:
            return node

        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.getheight(node.left),
                              self.getheight(node.right))
        new_root.height = 1 + \
            max(self.getheight(new_root.right), self.getheight(new_root.left))
        return new_root

    def print_tree(self):
        self.InorderPrint(self.root, 0)

    def InorderPrint(self, node, level):
        if node is not None:
            self.InorderPrint(node.right, level+1)
            # used this print line from the internet to make visualization easier
            print("    "*level + f"{node.val} ({node.frequency})")
            self.InorderPrint(node.left, level+1)


avl_tree_map = AVLTreeMap()

avl_tree_map.fileloader('D:/CISC235_testpath.txt')
avl_tree_map.print_tree()
