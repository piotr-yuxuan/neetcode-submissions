class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1

        def is_oob(i, j):
            return i < 0 or j < 0 or m <= i or n <= j

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                right_count = dp[i][j+1] if not is_oob(i, j+1) else 0
                bottom_count = dp[i+1][j] if not is_oob(i+1, j) else 0
                dp[i][j] += right_count + bottom_count

        return dp[0][0]
