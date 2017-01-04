class Listnode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


#data for test
no3 = Listnode(3)
no2 = Listnode(0)
no1 = Listnode(-1, no2)
no0 = Listnode(2, no1) 



def reorderList(head):
    # write your code here
    if head is None or head.next is None or head.next.next is None:
        return None
    length = 0
    tmp = head
    while tmp is not None:
        length += 1
        tmp = tmp.next
    i = 1
    tmp = head
    while i < length / 2:
        i += 1
        tmp = tmp.next
    newhead = tmp.next
    print(tmp.val)
    tmp.next = None

    def reverseList(head):
        if head is None or head.next is None:
            return head
        newhead = head
        head = head.next
        newhead.next = None
        
        while head is not None:
            tmp = head.next
            head.next = newhead
            newhead = head
            head = tmp

        return newhead

    newhead = reverseList(newhead)

    node1 = head
    node2 = newhead
    while node2 is not None:
        print("node1:", node1.val, "node2:", node2.val, "\n")
        tmp = node1.next
        node1.next = node2
        tmp2 = node2.next
        node2.next = tmp
        node1 = tmp
        node2 = tmp2



reorderList(no0)
head = no0
while head is not None:
    print(head.val, "\n")
    head = head.next
