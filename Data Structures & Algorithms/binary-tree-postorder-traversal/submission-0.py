from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def postorder(current, q):
            stack = []
            while current or stack:
                if current:
                    stack.append(current)
                    q.appendleft(current.val)
                    current = current.right
                else:
                    current = stack.pop()
                    current = current.left
            return q

        return list(postorder(root, deque()))
