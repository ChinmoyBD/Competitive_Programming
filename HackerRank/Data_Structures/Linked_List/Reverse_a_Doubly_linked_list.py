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

'''
def reverse(head):
    new_head = None

    while head:
        ne_xt = head.next
        new_head = head
        head.next = head.prev
        head.prev = ne_xt

        head = new_head
    return new_head
'''


def reverse(head):
    head.next, head.prev = head.prev, head.next

    if head.prev is None:
        return head
    return reverse(head.prev)


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_ndoe(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1)