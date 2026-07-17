from collections import deque
import functools


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjacency = [[i == j for j in range(numCourses)] for i in range(numCourses)]

        for n1, n2 in prerequisites:
            adjacency[n1][n2] = True

        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    adjacency[i][j] |= adjacency[i][k] and adjacency[k][j]

        return [adjacency[u][v] for u, v in queries]

    def _checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        flipped = {i: set() for i in range(numCourses)}
        for n1, n2 in prerequisites:
            flipped[n2].add(n1)

        path = set()
        ancestors = {i: set() for i in range(numCourses)}

        def dfs(node):
            for x in path:
                ancestors[x].add(node)
            if ancestors[node]:
                for x in path:
                    for y in ancestors[node]:
                        ancestors[x].add(y)
                return
            if node in path:
                return
            path.add(node)
            for child in flipped[node]:
                dfs(child)
            path.remove(node)

        for node in flipped.keys():
            dfs(node)

        return [u in ancestors[v] for u, v in queries]
