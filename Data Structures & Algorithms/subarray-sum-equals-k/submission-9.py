from collections import defaultdict
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        
        count = 0
        previous_sum = 0
        for i in range(len(nums)):
            prefix_sum = previous_sum + nums[i]

            if k == prefix_sum:
                count += 1
            count += prefix_sum_count[prefix_sum - k]

            prefix_sum_count[prefix_sum] += 1
            previous_sum = prefix_sum
        return count