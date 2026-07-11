class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def _ensure_node(self, n):
        if n not in self.parent:
            self.parent[n] = n
            self.rank[n] = 0

    def find(self, n):
        self._ensure_node(n)
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.rank[p1] += 1
            self.parent[p2] = p1

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind()
        for i in range(n):
            union_find.find(i)
        for e in edges:
            union_find.union(*e)
        return len(set(union_find.find(x) for x in union_find.parent.values()))
