from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()


    def _ensure_node(self, n):
        if n not in self.parent:
            self.parent[n] = n
        if n not in self.rank:
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
        
        if self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.rank[p1] += 1
            self.parent[p2] = p1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind()
        for account, *emails in accounts:
            e1 = emails[0]
            for e2 in emails[1:]:
                union_find.union(e1, e2)
        
        merged = defaultdict(set)
        for name, *emails in accounts:
            parent = union_find.find(emails[0])
            for e in emails:
                merged[(parent, name)].add(e)
        
        ret = list()
        for (parent, name), all_emails in merged.items():
            ret.append([name] + sorted(all_emails))
            
        return ret