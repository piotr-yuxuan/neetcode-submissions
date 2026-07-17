from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adjacency = {i:[] for i in range(n)}
        for (n1, n2) in edges:
            adjacency[n1].append(n2)
        
        visited = set()
        ret = list()
        path = set()
        def dfs(node):
            if node in path:
                return False
            if node not in adjacency:
                return True
            if node in visited:
                return True
            visited.add(node)
            path.add(node)
            for child in adjacency[node]:
                if not dfs(child):
                    return False
            path.remove(node)
            ret.append(node)
            return True
        
        for node in adjacency.keys():
            value = dfs(node)
            if not value:
                return []
        
        return list(reversed(ret))