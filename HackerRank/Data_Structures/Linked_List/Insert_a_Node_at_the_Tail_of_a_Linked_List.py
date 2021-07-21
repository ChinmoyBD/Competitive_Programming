class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkdList:
    def __init__(self):
        self.head = None


def _pritn(node):
    while node:
        print(node.data)

        node = node.next


def insertNodeAtTail(head, data):
    temp = head
    val = SinglyLinkedListNode(data)
    if head is None:
        head = val
    else:
        while temp.next:
            temp = temp.next
        temp.next = val
    return head


if __name__ == "__main__":
    n = int(input())

    llist = SinglyLinkdList()

    for i in range(n):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    _pritn(llist.head)