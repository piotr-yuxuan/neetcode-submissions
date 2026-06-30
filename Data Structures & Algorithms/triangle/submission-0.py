import functools


class Solution:
    def _minimumTotal(self, triangle: List[List[int]]) -> int:
        @functools.cache
        def dfs(i, j):
            if n - 1 == i:
                return triangle[i][j]
            elif len(triangle[i]) == j:
                return float("+inf")

            result = triangle[i][j] + min(
                dfs(i + 1, j),
                dfs(i + 1, j + 1),
            )
            return result

        return dfs(0, 0)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(i + 1):
                triangle[i][j] += min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1],
                )
        return triangle[0][0]
