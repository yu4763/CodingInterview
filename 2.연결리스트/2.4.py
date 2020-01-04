import singleLinkedList as sll

if __name__=="__main__":
    ll = sll.LinkedList([3, 5, 4, 7, 1, 2, 9, 8, 14])

    ll.print()
    print()

    x = int(input())

    cur = ll.head.next

    while cur.next is not None:
        v = int(cur.data)
        if v < x:
            ll.insert(v)
            cur = ll.deleteNode(cur)
        cur = cur.next

    ll.print()


