class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = -10**4

        for x in nums:
            if current_sum + x < x:
                current_sum = x
            else:
                current_sum = current_sum + x
            max_sum = max(max_sum, current_sum)
        
        return max_sum