from stack import Stack

if __name__ == "__main__":
    s = Stack([2, 5, 0, 9, 3, 5, 1])
    s.push(4)

    s.print()

    ss = Stack()

    while not s.isEmpty():

        if ss.isEmpty():
            new = s.pop()
            ss.push(new)
            continue

        cmp = ss.peek()
        new = s.pop()
        if new <= cmp:
            ss.push(new)
        else:
            while not ss.isEmpty():
                tmp = ss.peek()
                if tmp >= new:
                    break
                ss.pop()
                s.push(tmp)
            ss.push(new)

    ss.print()