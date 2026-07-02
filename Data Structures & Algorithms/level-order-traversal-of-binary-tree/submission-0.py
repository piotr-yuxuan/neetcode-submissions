from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([])
        q.append(root)
        res = []

        while q:
            level = []
            res.append([])
            while q:
                x = q.popleft()
                level.append(x)
                res[-1].append(x.val)
            for x in level:
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            
        return res