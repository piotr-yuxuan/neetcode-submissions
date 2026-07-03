# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def is_leaf(node):
            return not node.left and not node.right if node else False

        def dfs(node, target) -> False:
            remainder = target - node.val
            if 0 == remainder and is_leaf(node):
                return True
            elif node.left and dfs(node.left, remainder):
                return True
            elif node.right and dfs(node.right, remainder):
                return True
            return False
        
        return dfs(root, targetSum)
