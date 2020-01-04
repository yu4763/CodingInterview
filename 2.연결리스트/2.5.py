import singleLinkedList as sll

if __name__ == "__main__":
    ll1 = sll.LinkedList([7, 1, 6])
    ll2 = sll.LinkedList([5, 9, 2])

    n = ll1.num if ll1.num < ll2.num else ll2.num
    head1 = ll1.head.next
    head2 = ll2.head.next

    ll3 = sll.LinkedList()

    overflow = 0

    for i in range(n):
        print(head1.data)
        v = head1.data + head2.data + overflow

        if v >= 10:
            v -= 10
            overflow = 1
        else:
            overflow = 0

        ll3.insertTail(v)
        head1 = head1.next
        head2 = head2.next

    while head1.next is not None:
        v = head1.data + overflow
        if v >= 10:
            v -= 10
            overflow = 1
        else:
            overflow = 0
        ll3.insertTail(v)
        head1 = head1.next

    while head2.next is not None:
        v = head2.data + overflow
        if v >= 10:
            v -= 10
            overflow = 1
        else:
            overflow = 0
        ll3.insertTail(v)
        head2 = head2.next

    if overflow == 1:
        ll3.insertTail(1)


    ll1.print()
    print()
    ll2.print()
    print()
    ll3.print()

