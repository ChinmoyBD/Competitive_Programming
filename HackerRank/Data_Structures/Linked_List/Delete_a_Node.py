class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def _print(node):
    while node:
        print(node.data)

        node = node.next


def deleteNode(head, position):
    current_node = head
    if position is 0:
        head = head.next
    else:
        size = 1
        while size is not position:
            current_node = current_node.next
            size += 1
        current_node.next = current_node.next.next

    return head


if __name__ == "__main__":
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    _print(llist1)