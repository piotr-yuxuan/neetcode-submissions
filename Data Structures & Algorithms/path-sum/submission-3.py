# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node):
            if not node:
                return False

            return not node.left and not node.right

        def dfs(node, target) -> False:
            if not node:
                return False

            remainder = target - node.val

            if 0 == remainder and is_leaf(node):
                return True
            return dfs(node.left, remainder) or dfs(node.right, remainder)
        
        return dfs(root, targetSum)
