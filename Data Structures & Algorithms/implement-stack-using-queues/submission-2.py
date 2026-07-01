from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque([])
        self.size = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size += 1
        

    def pop(self) -> int:
        counter = self.size - 1
        self.size -= 1
        while 0 < counter:
            counter -= 1
            self.q.append(self.q.popleft())
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return 0 == self.size
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()