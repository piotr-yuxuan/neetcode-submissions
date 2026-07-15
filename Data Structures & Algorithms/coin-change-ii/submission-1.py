import functools

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @functools.cache
        def dfs(i, budget) -> int:
            if len(coins) <= i:
                return 0
            if 0 == budget:
                return 1
            elif budget < 0:
                return 0
            
            return dfs(i, budget-coins[i]) + dfs(i+1, budget)

        
        return dfs(0, amount)