class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()


    def _ensure_node(self, n):
        if n not in self.parent:
            self.parent[n] = n
        if n not in self.rank:
            self.rank[n] = 0
    
    
    def union(self, n1, n2):
        self._ensure_node(n1)
        self._ensure_node(n2)

        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p2] = p1
        if self.rank[p2] < self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.rank[p1] += 1
            self.parent[p2] = p1

        return True

    
    def find(self, n):
        self._ensure_node(n)

        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind()

        for (n1, n2) in edges:
            if not union_find.union(n1, n2):
                return [n1, n2]
        
        return []