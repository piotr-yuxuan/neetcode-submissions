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

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.rank[p1] += 1
            self.parent[p2] = p1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_streak = 0
        for n in nums:
            if n-1 in nums:
                continue
            current_streak = 0
            while n in nums:
                current_streak += 1
                n += 1
            max_streak = max(max_streak, current_streak)
        return max_streak

        
    def _longestConsecutive(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return 0

        nums = set(nums)
        union_find = UnionFind()
        for n in nums:
            if n + 1 in nums:
                union_find.union(n, n + 1)
        clusters = defaultdict(int)
        for x in nums:
            clusters[union_find.find(x)] += 1

        return max(clusters.values())
