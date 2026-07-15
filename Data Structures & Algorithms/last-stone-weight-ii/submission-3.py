import functools

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        target = sum(stones)//2

        @functools.cache
        def dfs(i, current_sum):
            if len(stones) == i:
                return current_sum

            option1 = dfs(i+1, current_sum)
            if current_sum + stones[i] <= target:
                option2 = dfs(i+1, current_sum + stones[i])
                if target-option2 <= target-option1:
                    return option2
            
            return option1

        return sum(stones)-2*dfs(0, 0)
