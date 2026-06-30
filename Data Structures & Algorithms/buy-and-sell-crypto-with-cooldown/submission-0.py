import functools

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Return the profit.
        @functools.cache
        def dfs(i, can_buy) -> int:
            if len(prices) <= i:
                return 0

            profit_noop = dfs(i+1, can_buy)
            if can_buy:
                profit_action = dfs(i+1, not can_buy) - prices[i]
            else:
                profit_action = dfs(i+2, not can_buy) + prices[i]
            return max(profit_noop, profit_action)

        return dfs(0, True)