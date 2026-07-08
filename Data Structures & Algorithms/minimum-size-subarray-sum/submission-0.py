class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums)+1

        current_sum = 0
        # Inclusive both ends.
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while target <= current_sum:
                min_length = min(min_length, right-left+1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if min_length == len(nums)+1 else min_length