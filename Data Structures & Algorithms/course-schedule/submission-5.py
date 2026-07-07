from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Course to required courses:
        adjacency = defaultdict(set)
        for left, right in prerequisites:
            adjacency[left].add(right)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if not adjacency[i]:
                return True
            
            children = adjacency[i]
            visited.add(i)
            for j in children:
                if not dfs(j):
                    return False
            visited.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True