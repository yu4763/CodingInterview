class Stack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, data):
        self.stack.insert(0, data)

        if len(self.min) == 0:
            self.min.append(data)
        else:
            if self.min[0] > data:
                self.min.insert(0, data)

    def pop(self):
        a = self.stack.pop(0)
        if a == self.min[0]:
            self.min.pop(0)

    def minV(self):
        if len(self.min) != 0:
            return self.min[0]
        else :
            return None

    def print(self):
        print(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(5)
    s.push(3)
    s.push(1)
    s.push(9)
    s.push(7)
    s.push(8)
    s.push(0)

    s.print()
    print(s.minV())

    while not s.isEmpty():
        s.pop()
        s.print()
        print(s.minV())



