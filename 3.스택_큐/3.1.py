
class Stack:
    def __init__(self):
        self.stack = []
        self.cnt1 = 0
        self.cnt2 = 0
        self.cnt3 = 0

    def push(self, data, num):
        if num == 0:
            self.stack.insert(0, data)
            self.cnt1 += 1
        elif num == 1:
            self.stack.insert(self.cnt1, data)
            self.cnt2 += 1
        else:
            self.stack.insert(self.cnt1 + self.cnt2, data)
            self.cnt3 += 1

    def pop(self, num):
        if num == 0:
            if self.cnt1 == 0:
                print('stack1 empty')
                return
            a = self.stack.pop(0)
            self.cnt1 -= 1
        elif num == 1:
            if self.cnt2 == 0:
                print('stack2 empty')
                return
            a = self.stack.pop(self.cnt1)
            self.cnt2 -=1

        else:
            if self.cnt3 == 0:
                print('stack3 empty')
                return
            a = self.stack.pop(self.cnt1 + self.cnt2)
            self.cnt3 -=1

        return a

    def isEmpty(self, num):
        if num == 0:
            if self.cnt1 == 0:
                return True
            return False
        elif num == 1:
            if self.cnt2 == 0:
                return True
            return False
        else :
            if self.cnt3 == 0:
                return True
            return False

    def peek(self, num):
        if self.isEmpty(num):
            print('empty')
            return
        if num == 0:
            return self.stack[0]
        elif num == 1:
            return self.stack[self.cnt1]
        else:
            return self.stack[self.cnt1 + self.cnt3]

    def print(self):
        for i in range(self.cnt1):
            print(self.stack[i], end=" ")
        print()
        for i in range(self.cnt1, self.cnt1+self.cnt2):
            print(self.stack[i], end=" ")
        print()
        for i in range(self.cnt1+self.cnt2, self.cnt1 + self.cnt2 + self.cnt3):
            print(self.stack[i], end=' ')
        print()



if __name__=='__main__':
    a = Stack()
    a.push(3, 0)
    a.push(6, 2)
    a.push(3, 2)
    a.push(1, 1)
    a.push(5, 0)
    a.push(9, 0)

    a.push(4, 1)
    a.push(8, 2)
    a.push(2, 1)

    a.print()

    a.pop(0)
    a.pop(3)

    print()
    a.print()
