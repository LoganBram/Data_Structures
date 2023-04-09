class Node:

    def __init__(self, d):
        self.data = d
        self.next = None


class LL:

    def __init__(self):
        self.head = None
        self.tail = None

    def FrontAdd(self, d):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def BackAdd(self, d):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def ReplaceAny(self, d, index):
        n = self.head
        for i in range(index):
            n = n.next
        n.data = d

    def FrontDelete(self):
        if self.head is None:
            pass
        else:
            self.head = self.head.next

    def BackDelete(self):
        if self.head is None:
            pass
        else:
            n = self.head
            while n.next != self.tail:
                n = n.next
            n.next = None
            self.tail = n

    def Print(self):
        current = self.head
        if self.head == None:
            return
        while current != None:
            print(current.data)
            current = current.next
