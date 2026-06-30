# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        dummy = ListNode()
        def step(current, list1, list2):
            if list2.val < list1.val:
                return step(current, list2, list1)

            current.next = list1
            current = list1
            list1 = list1.next

            return current, list1, list2
        
        current = dummy
        while current and list1 and list2:
            current, list1, list2 = step(current, list1, list2)

        if list1 is None:
            current.next = list2
        elif list2 is None:
            current.next = list1
        
        return dummy.next

