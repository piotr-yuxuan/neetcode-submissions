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

    
    def getNode(self, index: int) -> int:
        current = self.head
        while 0 < index:
            index -= 1
            if current is None:
                return None
            current = current.next
        return current

    def get(self, index: int) -> int:
        if node := self.getNode(index):
            return node.val
        else:
            return -1


    def insertHead(self, val: int) -> None:
        self.head = self.ListNode(val, self.head)
        self.tail = self.tail or self.head
        

    def insertTail(self, val: int) -> None:
        node = self.ListNode(val)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        self.head = self.head or self.tail
        

    def remove(self, index: int) -> bool:
        if 0 == index:
            if self.head is None:
                return False
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return True
            self.head = self.head.next
            return True

        current = self.getNode(index-1)
        if self.tail == current or current is None:
            return False

        if self.tail == current.next:
            self.tail = current
            current.next = None
            return True

        current.next = current.next.next
        return True


    def getValues(self) -> List[int]:
        return list(node.val for node in self)
