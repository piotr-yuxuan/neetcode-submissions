class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return 0
        if 1 == len(nums):
            return nums[0]

        max_sum = current_sum = nums[0]
        for x in nums[1:]:
            current_sum = max(current_sum + x, x)
            max_sum = max(max_sum, current_sum)
        
        return max_sum