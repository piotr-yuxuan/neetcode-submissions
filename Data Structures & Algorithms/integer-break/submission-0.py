import functools


class Solution:
    def integerBreak(self, n: int) -> int:

        # Return max product
        @functools.cache
        def dfs(i, s) -> int:
            if n == s:
                return 1
            elif n < s + i:
                return 1
            elif n < i + 1:
                return 1

            return max(
                i * dfs(i, s + i),
                dfs(i + 1, s),
            )

        return dfs(1, 0)
