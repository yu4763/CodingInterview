import singleLinkedList as sll

if __name__ == "__main__":
    ll = sll.LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])


    ll.print()
    print()

    k = int(input())
    temp = ll.head
    runner = temp
    for i in range(k):
        runner = runner.next
    temp = temp.next

    while runner.next.data != "tail":
        temp = temp.next
        runner = runner.next

    print(temp.data)