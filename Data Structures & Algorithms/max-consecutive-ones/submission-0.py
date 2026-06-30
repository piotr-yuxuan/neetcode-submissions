class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sum = current_sum = 0
        for i in range(len(nums)):
            current_sum = current_sum + 1 if 1 == nums[i] else 0
            max_sum = max(max_sum, current_sum)
        return max_sum