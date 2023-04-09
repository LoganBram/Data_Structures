class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.leng = 0
        self.head = None
        self.tail = None

    def append(self, data):
        newnode = Node(data)
        if self.tail is None:
            self.tail = newnode
            self.head = newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        self.leng += 1

    # reversal working
    def reverse(self):
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
