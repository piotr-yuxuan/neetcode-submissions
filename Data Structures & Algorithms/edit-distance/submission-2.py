import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)

        @functools.cache
        def dfs(i, j) -> int:
            if L1 <= i or L2 <= j:
                return max(0, L1 - i) + max(0, L2 - j)
            elif word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))

        return dfs(0, 0)
