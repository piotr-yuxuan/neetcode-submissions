import functools


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        max_length = 0

        @functools.cache
        def dfs(i, j) -> int:
            if j < i:
                return 0
            elif i == j:
                return 1

            if s[i] == s[j]:
                return 2 + dfs(i+1, j-1)
            else:
                return max(
                    dfs(i, j-1),
                    dfs(i+1, j),
                )
        
        return dfs(0, len(s)-1)
