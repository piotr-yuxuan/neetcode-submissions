# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def balanced_depth(node) -> int:
            if not node:
                return 0

            left = balanced_depth(node.left)
            if -1 == left:
                return -1
            right = balanced_depth(node.right)
            if -1 == right:
                return -1
            if 1 < abs(left-right):
                return -1
            return 1 + max(left, right)
        
        return -1 != balanced_depth(root)