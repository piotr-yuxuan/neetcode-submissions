import functools

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        target = sum(stones)//2

        # Return the minimal budget left to approach the target.
        @functools.cache
        def dfs(i, budget) -> int:
            if len(stones) == i:
                return budget

            option1 = dfs(i+1, budget)
            if 0 <= budget - stones[i]:
                option2 = dfs(i+1, budget - stones[i])
                if option2 <= option1:
                    return option2
            
            return option1

        return sum(stones)-2*(target-dfs(0, target))
