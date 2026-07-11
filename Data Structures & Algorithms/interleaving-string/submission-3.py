import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        @functools.cache
        def dfs(i, j):
            if l1 <= i and l2 <= j:
                return l3 == i + j
            if l3 <= i + j:
                return False

            value = False
            if i < l1 and s1[i] == s3[i + j]:
                value |= dfs(i + 1, j)
            if j < l2 and s2[j] == s3[i + j]:
                value |= dfs(i, j + 1)
            return value

        return dfs(0, 0)
