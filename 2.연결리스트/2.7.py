import singleLinkedList as sll

if __name__=="__main__":

    nodes = [sll.Node(3), sll.Node(2), sll.Node(5)]
    ll1 = sll.LinkedList()
    ll2 = sll.LinkedList()
    ll1.insertNodeLists(nodes)
    ll2.insertNodeLists(nodes)
    ll1.insert(4)
    ll1.insert(5)
    ll1.insert(6)
    ll2.insert(7)
    ll2.insert(1)
    ll2.insert(9)


    n1 = ll1.num
    n2 = ll2.num

    cur1 = ll1.head.next
    cur2 = ll2.head.next

    if n1 > n2:
        for i in range(n1 - n2):
            cur1 = cur1.next

    if n2 > n1:
        for i in range(n2 - n1):
            cur2 = cur2.next


    ans = []
    while cur1.data != "tail":
        if cur1 == cur2:
            ans.append(cur1)
        cur1 = cur1.next
        cur2 = cur2.next

    temp = ll1.head.next
    while temp.data != "tail":
        print(temp)
        temp = temp.next

    print()
    temp = ll2.head.next
    while temp.data != "tail":
        print(temp)
        temp = temp.next


    print(ans)
    for n in ans:
        print (n.data, end=" ")


# stack에 넣어서 pop하면서 tail을 비교해 나가는 방법도 존재.
