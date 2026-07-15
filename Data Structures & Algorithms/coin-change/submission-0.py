import functools


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Return min steps
        @functools.cache
        def dfs(i, budget) -> int:
            if budget < 0 or len(coins) == i:
                return -1
            if 0 == budget:
                return 0

            option1 = dfs(i+1, budget)
            option2 = dfs(i, budget-coins[i])
            if -1 == option2:
                return option1
            elif -1 == option1:
                return 1+option2
            else:
                return min(option1, 1+option2)
        
        return dfs(0, amount)