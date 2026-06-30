class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # The min cost to reach the top at this step.
        cost.append(0)
        cost.append(0)
        dp = cost
        for i in reversed(range(len(cost)-2)):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])
