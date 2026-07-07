class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for j in range(len(obstacleGrid[i]))] for i in range(len(obstacleGrid))]
        if not obstacleGrid[-1][-1]:
            dp[-1][-1] = 1

        def is_oob(i, j):
            return i < 0 or j < 0 or len(obstacleGrid) <= i or len(obstacleGrid[i]) <= j

        for i in reversed(range(len(obstacleGrid))):
            for j in reversed(range(len(obstacleGrid[i]))):
                if obstacleGrid[i][j]:
                    continue
                right_count = dp[i][j+1] if not is_oob(i, j+1) else 0
                bottom_count = dp[i+1][j] if not is_oob(i+1, j) else 0
                dp[i][j] += right_count + bottom_count

        return dp[0][0]
