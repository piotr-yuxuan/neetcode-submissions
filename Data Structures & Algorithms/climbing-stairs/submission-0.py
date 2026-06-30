class Solution:
    def _climbStairs(self, n: int) -> int:
        def dfs(n):
            if n < 3:
                return n
            return dfs(n-2) + dfs(n-1)

        return dfs(n)

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, len(dp)):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]