class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.stackNum = 0

    def push(self, data):
        if self.stackNum == 0:
            stack = [data]
            self.stacks.append(stack)
            self.stackNum += 1
        else:
            if len(self.stacks[0]) >= self.capacity:
                stack = [data]
                self.stacks.insert(0, stack)
                self.stackNum += 1
            else:
                stack = self.stacks[0]
                stack.insert(0, data)

    def pop(self):
        if self.stackNum == 0:
            print("empty")
            return
        else:
            stack = self.stacks[0]
            a = stack.pop(0)
            if len(stack) == 0:
                self.stacks.pop(0)
                self.stackNum -= 1
            return a

    def popAt(self, index):
        if self.stackNum <=  index:
            print("out of index")
            return
        else:
            stack = self.stacks[index]
            a = stack.pop(0)
            if len(stack) == 0:
                self.stacks.pop(index)
                self.stackNum -= 1

    def isEmpty(self):
        if self.stackNum == 0:
            return True
        else:
            return False

    def print(self):
        for i in range(self.stackNum):
            stack = self.stacks[i]
            for s in stack:
                print(s, end=" ")
            print()


if __name__ == "__main__":
    s = SetOfStacks(3)
    s.push(2)
    s.push(5)
    s.push(3)
    s.push(1)
    s.push(9)
    s.push(7)
    s.push(8)
    s.push(0)

    s.print()
    print(s.stackNum)
    print()

    s.popAt(1)
    s.print()
    print(s.stackNum)
    print()
    s.push(4)
    s.print()
    print(s.stackNum)
    print()
    s.push(5)
    s.print()
    print(s.stackNum)
    print()
    s.popAt(2)
    s.print()
    print(s.stackNum)
    print()
    s.popAt(2)
    s.print()
    print(s.stackNum)
    print()

    s.pop()
    s.print()
    print(s.stackNum)
    print()

    # while not s.isEmpty():
    #     a = s.pop()
    #     s.print()
    #     print("stack num: " + str(s.stackNum))
    #     print()
    #     if a == 9 or a == 1:
    #         s.push(15)
    #         s.print()
    #         print("stack num: " + str(s.stackNum))
    #         print()



