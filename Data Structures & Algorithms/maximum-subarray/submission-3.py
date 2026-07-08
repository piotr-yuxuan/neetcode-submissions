class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return 0
        if 1 == len(nums):
            return nums[0]

        # Inclusive left, exclusive right
        current_window = max_window = (0, 1)
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum+nums[i] < nums[i]:
                current_window = (i, i+1)
                current_sum = nums[i]
            else:
                current_window = (current_window[0], i+1)
                current_sum = current_sum + nums[i]
            if max_sum < current_sum:
                max_window = current_window
                max_sum = current_sum
        
        return max_sum
                