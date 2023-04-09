from LL import LL as LL

# doesnt work


def Swap(self, value1, value2):
    n = self.head
    prevNode1 = None
    prevNode2 = None
    node1 = self.head
    node2 = self.head

    while (node1 != None and node1.data != value1):
        prevNode1 = node1
        node1 = node1.next
    while (node2 != None and node1.data != value1):
        prevNode2 = node2
        node2 = node2.next
        if (node1 != None and node2 != None):
            if (prevNode1 != None):
                prevNode1.next = node2
            else:
                self.head = node2

            if (prevNode2 != None):
                prevNode2.next = node1
            else:
                self.head = node1

            temp = node1.next
            node1.next = node2.next
            node2.next = temp


# psuedo version
class LLStack:
    def __init__(self):
        self.stack = LL()

    def push(self, d):
        self.stack.FrontAdd(d)

    def pop(self):
        return self.stack.FrontDelete()

    def display(self):
        return self.stack.Print()

# actual version


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LLStackV2:

    def __init__(self):
        self.top = None

    def push(self, d):
        new_node = Node(d)
        if self.top == None:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        x = self.top.data
        self.top = self.top.next

    def print(self):
        n = self.top
        while n != None:
            print(n.data)
            n = n.next


class QueueStack:
    def __init__(self):
        self.bottom = None


class Manipulation(LL):

    def compare(self):
        acur = self.head
        bcur = b.head
        if self.head.data != bcur.data:
            return False
        while (acur and bcur) != None:
            if acur.data != bcur.data:
                return False
            acur = acur.next
            bcur = bcur.next
        return True

    # works
    def Reverse(self):
        prev = None
        current = self.head
        next = None
        print(current.data)
        while current.next is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = current

    # merges & sorts 2 LL of same size
    # identified numbers properly but issues with assigning numers to proper node in new LL
    # issue is in while loop and not assigning initial next head node i think
    def Merge(self, L1=LL(), L2=LL()):
        L1current = L1.head
        L2current = L2.head
        L3current = None
        if self.head == None:
            if L1current.data <= L2current.data:
                self.head = L1current
                L1current = L1current.next
            else:
                self.head = L2current
                L2current = L2current.next

        print(self.head.data, "here")
        while (L1current != None or L2current != None):

            if (L1current != None and L2current != None):
                if L1current.data <= L2current.data:
                    self.next = L1current
                    L1current = L1current.next
                    print(self.next.data, "here")
                    pass
                if L2current.data <= L1current.data:
                    self.next = L2current
                    L2current = L2current.next
                    print(self.next.data, "here")
                    pass

            if (L1current == None and L2current == None):
                return
            if (L1current != None and L2current == None):
                self.next = L1current
                L1current = L1current.next
                print(self.next.data, "here")

            if (L2current != None and L1current == None):
                self.next = L2current
                L2current = L2current.next
                print(self.next.data, "here")
        pass


q = Manipulation()
b = Manipulation()
q.FrontAdd(1)
q.FrontAdd(2)
q.FrontAdd(3)
b.FrontAdd(1)
b.FrontAdd(2)
b.FrontAdd(3)
print(b.compare())
