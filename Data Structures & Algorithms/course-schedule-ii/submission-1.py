class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = {i: list() for i in range(numCourses)}
        for n1, n2 in prerequisites:
            adjacency[n1].append(n2)
        path = set()
        visited = set()
        topo_sort = list()

        def dfs(node):
            if node in path:
                return False
            if node is None:
                return True
            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)
            for child in adjacency[node]:
                if not dfs(child):
                    return False

            path.remove(node)
            topo_sort.append(node)
            return True
        
        for node in adjacency:
            if not dfs(node):
                return []

        return topo_sort
        