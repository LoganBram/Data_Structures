from LL import LL as LL


class LLStack:
    def __init__(self):
        self.stack = LL()

    def push(self, d):
        self.stack.FrontAdd(d)

    def pop(self):
        return self.stack.FrontDelete()

    def display(self):
        return self.stack.Print()


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


q = LLStackV2()
q.push(10)
q.push(20)
q.push(30)
q.pop()
q.pop()
q.print()
