# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        origin = ListNode(float('-inf'))
        while head:
            head_next = head.next
            previous = origin

            while previous.next and previous.next.val < head.val:
                previous = previous.next

            head.next = previous.next
            previous.next = head

            head = head_next

        return origin.next