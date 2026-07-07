from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Course to required courses:
        adjacency = defaultdict(set)
        for left, right in prerequisites:
            adjacency[left].add(right)
        
        visited = dict({})        
        def dfs(i, local_visited) -> bool:
            if i in local_visited:
                return False
            if i in visited:
                return visited[i]

            children = adjacency.get(i, None)
            if not children:
                visited[i] = True
                return True
            
            local_visited.add(i)
            value = True
            for c in children:
                if not dfs(c, local_visited):
                    value = False
                    break
            local_visited.remove(i)
            visited[i] = value
            return value
      
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True
