class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # Memoisation table

        def dfs(i: int, j: int) -> int:
            if dp[i][j] != 0:
                return dp[i][j]
            x = matrix[i][j]

            dp[i][j] = 1 + max(
                dfs(i-1, j  ) if i > 0   and matrix[i-1][j] > x else 0,
                dfs(i+1, j  ) if i < m-1 and matrix[i+1][j] > x else 0,
                dfs(i  , j-1) if j > 0   and matrix[i][j-1] > x else 0,
                dfs(i  , j+1) if j < n-1 and matrix[i][j+1] > x else 0
            )

            return dp[i][j]

        return max(dfs(i, j) for i in range(m) for j in range(n))