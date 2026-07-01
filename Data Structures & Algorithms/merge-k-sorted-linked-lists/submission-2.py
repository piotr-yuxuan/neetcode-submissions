# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def sort_key(node: ListNode) -> int:
            return node.val

        def filter_and_sort(lists):
            return sorted(
                filter(lambda x: x is not None, lists),
                key=sort_key,
            )

        lists = filter_and_sort(lists)
        if not lists:
            return None

        origin = current = lists[0]
        lists[0] = lists[0].next

        lists = filter_and_sort(lists)
        while lists:
            current.next = lists[0]
            lists[0] = lists[0].next
            current = current.next

            lists = filter_and_sort(lists)
        
        return origin
