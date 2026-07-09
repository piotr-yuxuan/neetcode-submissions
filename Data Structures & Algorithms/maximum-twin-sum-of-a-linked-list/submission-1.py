# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"val={self.val}"

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the last half
        tail, current = slow, slow.next
        tail.next = None
        while current:
            tail, current.next, current = current, tail, current.next

        # Compute maximum sum
        max_sum = -1
        while head and tail:
            max_sum = max(max_sum, head.val + tail.val)
            head, tail = head.next, tail.next

        return max_sum
        # Get hired :)