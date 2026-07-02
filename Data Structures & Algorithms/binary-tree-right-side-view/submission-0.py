from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return [] 
       
        res = []
        q = deque([])
        q.append(root)

        while q:
            level = []
            while q:
                level.append(q.popleft())
            res.append(level[-1].val)
            for x in level:
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        
        return res
