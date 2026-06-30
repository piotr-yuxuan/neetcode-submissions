class LinkedList:
    
    class ListNode():
        def __init__(self, val, next = None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    
    def _get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def get(self, index: int) -> int:
        if node := self._get(index):
            return node.val
        else:
            return -1


    def insertHead(self, val: int) -> None:
        self.head = self.ListNode(val, self.head)
        self.tail = self.tail or self.head
        print('insertHead', self.getValues(), f"head={self.head.val}", f"tail={self.tail.val}")
        

    def insertTail(self, val: int) -> None:
        node = self.ListNode(val)
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.head = self.head or self.tail
        print('insertTail', self.getValues(), f"head={self.head.val}", f"tail={self.tail.val}")
        

    def remove(self, index: int) -> bool:
        if 0 == index:
            if self.head is None:
                return False
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return True
            self.head = self.head.next
            print('remove', self.getValues(), f"head={self.head.val}", f"tail={self.tail.val}")
            return True

        current = self._get(index-1)
        if self.tail == current or current is None:
            print('remove', self.getValues(), f"head={self.head.val}", f"tail={self.tail.val}")
            return False

        if self.tail == current.next:
            self.tail = current
            current.next = None
            print('remove', self.getValues(), f"head={self.head.val}", f"tail={self.tail.val}")
            return True

        current.next = current.next.next
        print('remove', self.getValues(), f"head={self.head.val}", f"tail={self.tail.val}")
        return True


    def getValues(self) -> List[int]:
        return list(node.val for node in self)
