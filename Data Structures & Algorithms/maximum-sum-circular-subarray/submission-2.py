class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return 0
        if 1 == len(nums):
            return nums[0]

        min_sum = max_sum = current_max_sum = current_min_sum = nums[0]
        for x in nums[1:]:
            current_max_sum = max(current_max_sum+x, x)
            max_sum = max(current_max_sum, max_sum)

            current_min_sum = min(current_min_sum+x, x)
            min_sum = min(current_min_sum, min_sum)

        print(max_sum, min_sum)
        if 0 == sum(nums) - min_sum:
            return max_sum
        else:
            return max(max_sum, sum(nums) - min_sum)