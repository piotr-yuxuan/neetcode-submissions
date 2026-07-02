# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        n = k
        res = -1

        def inorder(node):
            nonlocal n, res
            if not node or 0 == n:
                return
            
            inorder(node.left)
            n -= 1
            if 0 == n:
                res = node.val
            inorder(node.right)

        inorder(root)
        return res