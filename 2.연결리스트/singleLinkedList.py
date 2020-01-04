class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, lists=[]):
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.num = 0
        for i in lists[::-1]:
            self.insert(i)

    def insert(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.num += 1

    def insertTail(self, data):
        newTail = Node("tail")
        self.tail.data = data
        self.tail.next = newTail
        self.tail = newTail
        self.num += 1

    def insertNodeLists(self, lists):
        for i in lists[::-1]:
            i.next = self.head.next
            self.head.next = i
            self.num += 1

    def delete(self, index):
        if index > self.num or index <= 0:
            return False
        else:
            cur = self.head.next
            for i in range(index-1):
                cur = cur.next
            cur.next.next = cur.next
            self.num -= 1

    def deleteNode(self, node):
        run = self.head
        tt = run.next
        find = False
        while run.next is not None:
            if tt == node:
                find = True
                break
            run = run.next
            tt = run.next

        if find:
            run.next = tt.next
            self.num -= 1

        return run

    def print(self):
        tt = self.head.next
        while tt.next is not None:
            print(tt.data, end=" ")
            tt = tt.next

