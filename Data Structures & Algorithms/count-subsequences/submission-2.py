import functools

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        path = []
        @functools.cache
        def dfs(i, j) -> int:
            if len(t) == j:
                return 1
            if len(s) <= i:
                return 0

            value = dfs(i+1, j)
            if s[i] == t[j]:
                value += dfs(i+1, j+1)

            return value

        return dfs(0, 0)
