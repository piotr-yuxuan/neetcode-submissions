# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, l):
            if node:
                l.append(node.val)
                dfs(node.left, l)
                dfs(node.right, l)
            return l
        # return dfs(root, list())

        def preorder (node, l):
            stack = []
            current = node
            while stack or current:
                if current:
                    stack.append(current)
                    l.append(current.val)
                    current = current.left
                else:
                    current = stack.pop()
                    current = current.right
            return l
        
        return preorder(root, list())

            
