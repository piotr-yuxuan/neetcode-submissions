# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        prev, current = None, head
        while current.next:
            print(current.val)
            next_node = current.next
            current.next = prev
            prev, current = current, next_node
        current.next = prev
        return current