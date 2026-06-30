from typing import Optional

class BrowserHistory:

    class ListNode:
        def __init__(
            self,
            val: str,
            prev: Optional[ListNode] = None,
            next: Optional[ListNode] = None,
        ):
            self.val = val
            self.prev = prev
            self.next = next


    def __init__(self, homepage: str):
        self.current = self.ListNode(homepage)


    def visit(self, url: str) -> None:
        node = self.ListNode(url, prev=self.current)
        self.current.next = node
        self.current = node
        

    def back(self, steps: int) -> str:
        while 0 < steps:
            if self.current.prev is None:
                break

            self.current = self.current.prev
            steps -= 1

        return self.current.val
        

    def forward(self, steps: int) -> str:
        while 0 < steps:
            if self.current.next is None:
                break
            
            self.current = self.current.next
            steps -= 1

        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)