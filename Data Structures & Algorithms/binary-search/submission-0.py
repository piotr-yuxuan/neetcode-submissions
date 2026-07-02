class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if 1 == len(nums):
            return 0 if target == nums[0] else -1

        # Inclusive left, inclusive right.
        left = 0
        right = len(nums)-1

        while left <= right:
            midpoint = (left+right) // 2
            if target < nums[midpoint]:
                right = midpoint - 1
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                return midpoint
        
        return -1