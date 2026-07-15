import functools


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        # (ith element, remaining capacity) → profit
        @functools.cache
        def dfs(i, budget) -> int:
            if len(profit) <= i:
                return 0
            
            return max(
                dfs(i+1, budget),
                profit[i] + dfs(i, budget - weight[i]) if 0 <= budget - weight[i] else 0
            )

        return dfs(0, capacity)