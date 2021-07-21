from ds import DoubleLinkedList


class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        if not self.is_empty():
            val = self.__list.back()
            self.__list.remove_last()
            return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size


class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self, val):
        self.__list.add(val)

    def deque(self):
        val = self.__list.front()
        self.__list.remove_first()
        return val

    def front(self):
        return self.__list.front()

    def __len__(self):
        return self.__list.size

    def is_empty(self):
        return self.__list.size == 0


# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# print(my_stack.peek())
# my_stack.push(5)
# print(len(my_stack))
# my_stack.pop()
# print(len(my_stack))

my_queue = Queue()
my_queue.enqueue(1)
print(len(my_queue))
print(my_queue.front())
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.deque()
print(my_queue.front())
print(len(my_queue))