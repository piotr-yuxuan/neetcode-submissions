import functools


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        if 2 == len(nums):
            return nums[0] == nums[1]

        target = sum(nums)/2
        if not target.is_integer():
            return False

        @functools.cache        
        def dfs(target, i) -> bool:
            if len(nums) == i:
                return False
            elif 0 == target:
                return True
            
            return dfs(target - nums[i], i+1) or dfs(target , i+1)
        
        return dfs(target, 0)