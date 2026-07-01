class ListNode():
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class Deque:
    
    def __init__(self):
        self.array = []
        self.tail = None
        self.head = None


    def __iter__(self):
        current = self.tail
        while current:
            yield current
            current = current.next


    def isEmpty(self) -> bool:
        return self.head is None
        

    def append(self, value: int) -> None:
        node = ListNode(value=value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        

    def appendleft(self, value: int) -> None:
        node = ListNode(value=value)
        if self.tail is None:
            self.tail = self.head = node
        else:
            node.next = self.tail
            self.tail.prev = node
            self.tail = node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = node.prev

        return node.value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        node = self.tail
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = node.next

        return node.value
