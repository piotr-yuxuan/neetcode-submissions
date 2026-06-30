import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @functools.cache
        def dfs(i, current):

            if len(nums) == i:
                if target == current:
                    return 1
                else:
                    return 0
            if len(nums) <= i:
                return 0
            
            _1 = dfs(i + 1, current + nums[i])
            _2 = dfs(i + 1, current - nums[i])
            return _1 + _2


        return dfs(0, 0)