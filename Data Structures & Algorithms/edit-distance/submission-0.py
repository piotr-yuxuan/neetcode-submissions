import functools

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Return the number of operations performed
        @functools.cache
        def dfs(i, j):
            if len(word1) == i:
                return len(word2) - j
            elif len(word2) == j:
                return len(word1) - i
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                return 1 + min(dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1))
        
        return dfs(0, 0)