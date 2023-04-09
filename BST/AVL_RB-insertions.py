class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = None


class AVL_Tree(TreeNode):

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif root.val < key:
            root.left = self.insert(root.left, key)
        elif root.val > key:
            root.right = self.insert(root.right, key)

        # step 2, update height of ancestor
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # update balance factor
        balance = self.getBalance(root)

        # step 4 try imbalance cases
        # if imbalance is on left side & its left left
        if balance < -1 and key < root.left.val:
            return self.rightRotate(root)
        # if on right side and key is greater then the right child, aka right right
        if balance > 1 and key > root.right.val:
            return self.leftRotate(root)

        # if on left side and key is greater then left value, aka left -> right
        if balance < -1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance > 1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

    def _leftRotate(self, A):
        B = A.right
        beta = B.left

        # perform rotation
        B.left = A
        A.right = beta

        # update height
        A.height = 1 + max(self.getHeight(A.left). self.getHeight(A.right))
        B.height = 1 + max(self.getHeight(B.left), self.getHeight(B.right))

        return B

    def _rightRotate(self, B):
        A = B.left
        beta = A.right

        # Perform Rotation
        A.right = B
        B.left = beta

        # update heights
        B.height = 1 + max(self.getHeight(B.left), self.getHeight(B.right))
        A.height = 1 + max(self.getHeight(A.left), self.getHeight(B.left))

        return A


class RBNode():

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.color = "R"


class RB_Tree(RBNode):

    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self._insert(self.root, x)
        self.root.color = "B"
        print(self.root.val)

    def _insert(self, node, key):
        # insert recursively
        if node == None:
            return RBNode(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
            # once insert on left completes
            # if left of parent is black, all good
            if node.left.color == "B":
                return node
            else:
                if (node.left.left.color == "R") or (node.left.right.color == "R"):
                    if node.left.left.color == "R":
                        # do left left rotate
                        return self.LeftLeft(node)
                    else:
                        self.LeftRight(node)

                else:
                    return node
        elif key > node.val:
            # insert to right side
            node.right = self._insert(node.right, key)

            # once done, check if parent on right side is black
            if node.right.color == "B":
                return node
            else:

                if (node.right.right.color == "R") or (node.right.left.color == "R"):
                    if node.right.right == "R":
                        return self.RightRight(node)
                    else:
                        return self.RightLeft(node)
                else:
                    return node

    def RightRight(self, GP):
        # now check two cases, if aunt is red change colors of all 3
        parent = GP.right
        aunt = GP.left

        if aunt.color == "R":
            GP.color = "R"
            parent.color = "B"
            aunt.color = "B"

            return GP
        else:
            # aunt is black
            # rotate
            GP.right = parent.left
            parent.left = GP
            # color change
            GP.color = "R"
            parent.color = "B"

            return parent

    def RightLeft(self, GP):
        # if aunt red,
        aunt = GP.left
        parent = GP.right
        if aunt.color == "R":
            parent.color = "B"
            aunt.color = "B"
            GP.color = "R"
            return GP
        else:
            # aunt is black, double rotate and color change
            C = parent.left
            parent.left = C.right
            C.right = parent
            # first rotate
            GP.right = C.left
            C.left = GP
            # second rotate done
            C.color = "B"
            GP.color = "R"
            # color change
            return C

    def LeftLeft(self, GP):
        parent = GP.left
        aunt = GP.right
        # case 1, aunt is red
        if aunt.color == "R":
            GP.color = "R"
            parent.color = "B"
            aunt.color = "B"

            return GP
        else:
            # aunt is black with left left, parent and gp switch colors then right rotate
            # rotate
            GP.leftchild = parent.rightchild
            parent.rightchild = GP
            # recolor
            parent.color = "B"
            GP.color = "R"

            return parent

    def LeftRight(self, GP):
        # check if aunt is red, if yes recolor
        parent = GP.left
        aunt = GP.right

        if aunt.color == "R":
            parent.color = "B"
            GP.color = "R"
            aunt.color = "B"
            return GP
        # if aunt is black then double rotate and recolor
        else:
            C = parent.right
            parent.right = C.left
            C.left = parent
            # left rotation done
            GP.left = C.right
            C.right = GP
            # right rotation done
            C.color = "B"
            GP.color = "R"

            # return root
            return C


q = RB_Tree()
q.insert(1)
q.insert(2)
q.inert(3)
