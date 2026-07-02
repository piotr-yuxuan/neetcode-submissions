from itertools import islice
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def walk(node):
            if not node:
                return
            yield from walk(node.left)
            yield node.val
            yield from walk(node.right)

        return next(islice(walk(root), k-1, None))