class ListNode():
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.left = None
        self.right = None
        self.size, self.k = 0, k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = ListNode(value=value)
        self.size += 1

        if 1 == self.size:
            self.left = self.right = node
        else:       
            node.prev = self.right
            self.right.next = node
            self.right = node

        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1

        if 0 == self.size:
            self.left = self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None
        
        return True


    def Front(self) -> int:
        return -1 if self.isEmpty() else self.left.value


    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.right.value


    def isEmpty(self) -> bool:
        return 0 == self.size 
        

    def isFull(self) -> bool:
        return self.k == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()