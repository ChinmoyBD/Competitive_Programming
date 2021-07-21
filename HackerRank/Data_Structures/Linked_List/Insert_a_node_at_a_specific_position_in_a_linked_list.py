class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkdList:
    def __init__(self):
        self.head = None


def _print(node):
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


def insertAtPosition(head, data, position):
    current_node = head
    size = 1
    new_node = SinglyLinkedListNode(data)

    if position is 0:
        head = new_node
        new_node.next = current_node
    else:
        while size != position:
            current_node = current_node.next
            size += 1

        new_node.next = current_node.next
        current_node.next = new_node

    return head


if __name__ == "__main__":
    n = int(input())

    llist = SinglyLinkdList()

    for i in range(n):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    data = int(input())
    position = int(input())

    llist_head = insertAtPosition(llist.head, data, position)

    _print(llist_head)