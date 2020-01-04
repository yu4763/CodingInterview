class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None


class LinkedList:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.before = self.head
        self.num = 0

    def insert(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        node.next.before = node
        node.before = self.head
        self.num += 1

    def delete(self, index):
        if index > self.num or index <= 0:
            return False
        else:
            tt = self.head
            for i in range(index):
                tt = tt.next
            tt.before.next = tt.next
            tt.next.before = tt.before
            self.num -= 1

    def deleteNode(self, node):
        tt = self.head
        find = False
        while tt.next is not None:
            tt = tt.next
            if tt == node:
                find = True
                break
        if find:
            tt.before.next = tt.next
            tt.next.before = tt.before
            self.num -= 1

        return tt.before

    def print(self):
        tt = self.head.next
        while tt.next is not None:
            print(tt.data, end=" ")
            tt = tt.next

