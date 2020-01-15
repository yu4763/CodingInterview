from stack import Stack

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        if self.s2.isEmpty():
            if self.s1.isEmpty():
                print("empty")
                return
            else:
                while not self.s1.isEmpty():
                    a = self.s1.pop()
                    self.s2.push(a)
                return self.s2.pop()
        else:
            return self.s2.pop()

    def isEmpty(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            return True
        else:
            return False

if __name__ == "__main__":
    s = MyQueue()
    s.enqueue(2)
    s.enqueue(5)
    s.enqueue(6)
    s.enqueue(1)
    s.enqueue(9)
    s.enqueue(24)

    while not s.isEmpty():
        print(s.dequeue())
