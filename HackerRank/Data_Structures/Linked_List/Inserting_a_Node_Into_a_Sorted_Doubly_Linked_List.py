class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_ndoe(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node):
    while node:
        print(node.data)

        node = node.next


def sortedInsert(head, data):
    temp = head
    node = DoublyLinkedListNode(data)
    if temp.data >= data:
        temp.prev = node
        node.next = temp
        head = temp.prev
    else:
        while temp.next:
            if temp.next.data >= data:
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next

        if temp.next is None:
            temp.next = node

    return head


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_ndoe(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1)