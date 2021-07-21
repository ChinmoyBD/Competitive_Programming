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


def print_singly_linked_list(node):
    while node:
        print(node.data)

        node = node.next


def mergeLists(head1, head2):
    temp1 = temp2 = None
    if head1.data < head2.data:
        temp1 = head1
        temp2 = head2
    else:
        temp1 = head2
        temp2 = head1

    llist = SinglyLinkedList()

    while temp1:
        llist.insert_node(temp1.data)

        while temp2:
            if not temp1.next:
                llist.insert_node(temp2.data)
            else:
                if temp2.data <= temp1.next.data:
                    llist.insert_node(temp2.data)
                else:
                    break

            temp2 = temp2.next

        temp1 = temp1.next

    return llist.head


if __name__ == "__main__":
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())
        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3)

