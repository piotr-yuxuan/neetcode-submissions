import functools


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @functools.cache
        def dfs(i, j) -> int:
            if len(text1) <= i or len(text2) <= j:
                value = 0
            elif text1[i] == text2[j]:
                value = 1 + dfs(i+1, j+1)
            else:
                value = max(
                    dfs(i+1, j),
                    dfs(i, j+1),
                    dfs(i+1, j+1),
                )
            return value

        return dfs(0, 0)
