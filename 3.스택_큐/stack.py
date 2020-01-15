class Stack:
    def __init__(self, data = []):
        data.reverse()
        self.stack = data

    def push(self, data):
        self.stack.insert(0, data)

    def pop(self):
        if self.isEmpty():
            print("empty")
            return
        a = self.stack.pop(0)
        return a

    def peek(self):
        if self.isEmpty():
            print("empty")
            return
        return self.stack[0]

    def print(self):
        print(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
