from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(existing, seen):
            if existing in seen:
                return seen[existing]
            if existing is None:
                return
            
            cloned = Node(existing.val)

            seen[existing] = cloned
            for node in existing.neighbors:
                cloned.neighbors.append(dfs(node, seen))
            seen
            return cloned
        
        return dfs(node, dict())
