import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @functools.cache
        def dfs(s, i) -> int:
            if len(nums) == i:
                return 1 if s == target else 0

            return dfs(s + nums[i], i+1) + dfs(s - nums[i], i+1)
        
        return dfs(0, 0)