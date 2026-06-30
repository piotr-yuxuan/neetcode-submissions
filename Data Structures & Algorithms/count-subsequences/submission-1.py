import functools

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        _s, _t = len(s), len(t)

        if _s < _t:
            return 0
        
        @functools.cache
        def dfs(i, j):
            if _t == j:
                return 1
            if _s == i:
                return 0

            return dfs(i+1,j) + (dfs(i+1,j+1) if s[i] == t[j] else 0)

        return dfs(0, 0)
