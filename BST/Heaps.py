from queue import Queue


class HeapNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MaxHeap(HeapNode):

    def __init__(self):
        self.heap = []
        self.root = None

    def insert(self, x):

        if self.root == None:
            node = HeapNode(x)
            self.root = node
            self.heap.append(x)
        else:
            # attatch value to bottom of array
            self.heap.append(x)
            # get index of value
            index = len(self.heap) - 1
            parent_index = (index-1)//2
            while index > 0:
                parent_index = (index - 1)//2
                if self.heap[parent_index] < self.heap[index]:
                    self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                    index = parent_index
                else:
                    break
            print(self.heap)


class MinHeap(HeapNode):

    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)


b = MaxHeap()
b.insert(3)
b.insert(4)
b.insert(2)
b.insert(9)
