# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:            
        def merge(list1, list2):
            origin = ListNode()
            current = origin
            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    current = current.next
                    list1 = list1.next
                else:
                    list1, list2 = list2, list1
            if list1:
                current.next = list1
            else:
                current.next = list2
            return origin.next
        
        if not lists:
            return None
        elif 1 == len(lists):
            return lists[0]
        elif 2 == lists[0]:
            return merge(*lists)
        
        while 1 < len(lists):
            lists = [
                merge(
                    lists[i],
                    lists[i+1] if i+1 < len(lists) else None) 
                for i in range(0, len(lists), 2)
            ]
        
        return lists[0]




















