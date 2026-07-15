import functools


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # Maximise profit within capacity

        # Return profit
        @functools.cache
        def dfs(i, budget) -> int:
            if len(profit) == i:
                return 0

            option1 = dfs(i + 1, budget)
            if 0 <= budget - weight[i]:
                option2 = profit[i] + dfs(i + 1, budget - weight[i])
                return max(option1, option2)
            return option1

        return dfs(0, capacity)
