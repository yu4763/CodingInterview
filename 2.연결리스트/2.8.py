class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, lists=[]):
        self.head = Node("head")
        self.num = 0
        for i in lists[::-1]:
            i.next = self.head.next
            self.head.next = i
            self.num += 1

    def insert(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
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


if __name__ == "__main__":
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]
    ll = LinkedList(nodes)
    temp = ll.head
    while temp.next != None:
        temp = temp.next
    temp.next = nodes[2]

    visited = dict()
    temp = ll.head
    ans = None

    while temp.next is not None:
        temp = temp.next
        if temp in visited.keys():
            ans = temp
            break
        else:
            visited[temp] = True

    print(ans)
    if ans is not None:
        print(ans.data)