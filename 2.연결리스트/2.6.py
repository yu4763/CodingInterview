import singleLinkedList as sll

if __name__ == "__main__":
    ll = sll.LinkedList([1, 4, 6,5, 3, 6, 4, 1,])
    reverse = sll.LinkedList()

    cur = ll.head.next
    while cur.data != "tail":
        reverse.insert(cur.data)
        cur = cur.next

    cur1 = ll.head.next
    cur2 = reverse.head.next
    n = ll.num
    palindrome = True

    ll.print()
    print()
    reverse.print()
    print()

    for i in range(n):
        if cur1.data != cur2.data:
            palindrome = False
            break
        cur1 = cur1.next
        cur2 = cur2.next

    print(palindrome)