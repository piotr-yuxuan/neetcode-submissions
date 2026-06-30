# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        previous, current = None, head

        for i in range(1, left):
            previous = current
            current = current.next

        outer_left_pointer = previous
        previous = None

        reversal_start = current
        i = left
        while current and i <= right:
            i += 1
            current.next, previous, current = previous, current, current.next

        if current:
            outer_right_pointer = current.next
        if outer_left_pointer:
            outer_left_pointer.next = previous

        reversal_start.next = current

        return previous if left == 1 else head