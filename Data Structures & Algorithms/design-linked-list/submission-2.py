from typing import Optional

class MyLinkedList:

    class ListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next


    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
        

    def getNode(self, index: int) -> Optional[ListNode]:
        current = self.head
        while 0 < index and current is not None:
            current = current.next
            index -= 1
        return current

    
    def get(self, index: int) -> int:
        if node := self.getNode(index):
            return node.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        node = self.ListNode(val=val)
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        if self.tail is None:
            self.tail = node
        

    def addAtTail(self, val: int) -> None:
        node = self.ListNode(val=val)
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        if self.head is None:
            self.head = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 == index:
            self.addAtHead(val)
            return
        prev = self.getNode(index-1)
        if self.tail == prev:
            self.addAtTail(val)
            return
    
        next = prev.next
        node = self.ListNode(val=val, prev=prev, next=next)
        prev.next = next.prev = node
        

    def deleteAtIndex(self, index: int) -> None:
        if 0 == index:
            if self.head == self.tail:
                self.head = self.tail = None
                return
            node = self.head
            self.head = node.next
            self.head.prev = None
            return
        node = self.getNode(index)
        if node is None:
            return
        if self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            return
        
        node.prev.next, node.next.prev = node.next, node.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)