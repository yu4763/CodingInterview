import doubleLinkedList as dll

def removeRepeat(ll):
    temp = ll.head
    values = []
    while temp.next is not None:
        temp = temp.next
        v = temp.data
        if v in values:
            temp = ll.deleteNode(temp)
        else:
            values.append(v)
    return ll


def removeRepeatWoBuffer(ll):
    temp = ll.head
    while temp.next is not None:
        temp = temp.next
        runner = temp
        v = temp.data
        while runner.next is not None:
            runner = runner.next
            rv = runner.data
            if rv == v:
                runner = ll.deleteNode(runner)

    return ll

if __name__ == "__main__":
    ll = dll.LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(10)
    ll.insert(5)
    ll.insert(7)
    ll.insert(2)
    ll.insert(1)
    ll.insert(3)
    ll.insert(7)

    ll.print()
    print()

    # ll = removeRepeat(ll)
    # ll.print()
    # print()

    ll = removeRepeatWoBuffer(ll)
    ll.print()
    print()

