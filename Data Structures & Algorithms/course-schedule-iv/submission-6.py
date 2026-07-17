from collections import deque
import functools


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        flipped = {i:set() for i in range(numCourses)}
        for n1, n2 in prerequisites:
            flipped[n2].add(n1)

        path = set()
        ancestors = {i:set() for i in range(numCourses)}
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
