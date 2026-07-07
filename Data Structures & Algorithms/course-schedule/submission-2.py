from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Course to required courses:
        adjacency = defaultdict(set)
        for i in range(numCourses):
            adjacency[i] = set()
        for left, right in prerequisites:
            adjacency[left].add(right)
        
        taken = set()
        
        while True:
            possible = set()
            for k, v in list(adjacency.items()):
                if not v:
                    possible.add(k)
                    adjacency.pop(k)

            for k in adjacency.keys():
                adjacency[k] = adjacency[k].difference(possible)

            taken = taken.union(possible)

            if not possible:
                break

        return numCourses <= len(taken)