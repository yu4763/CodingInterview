import singleLinkedList as sll

if __name__ == "__main__":
    ll = sll.LinkedList()
    ll.insert(9)
    ll.insert(8)
    ll.insert(7)
    ll.insert(6)
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)

    ll.print()
    print()

    d = ll.head.next.next.next
    d.data = d.next.data
    d.next = d.next.next

    ll.print()
