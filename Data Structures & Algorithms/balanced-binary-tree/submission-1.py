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

        res = True
        def balanced_depth(node) -> int:
            nonlocal res
            if not node or not res:
                return 0

            left = balanced_depth(node.left)
            right = balanced_depth(node.right)
            if 1 < abs(left-right):
                res = False
            return 1 + max(left, right)
        
        balanced_depth(root)
        
        return res