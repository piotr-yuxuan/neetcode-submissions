from collections import defaultdict
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        
        count = 0
        previous_sum = 0
        for i in range(len(nums)):
            #print(f"=== {i=}")
            prefix_sum = previous_sum + nums[i]
            #print(f"{dict(prefix_sum_count)=}, {prefix_sum=}")

            if k == prefix_sum:
                #print("DEBUG_1")
                count += 1
            shorter_sum = prefix_sum - k
            #print(f"{shorter_sum=}, {prefix_sum_count[shorter_sum]=}")
            count += prefix_sum_count[shorter_sum]

            prefix_sum_count[prefix_sum] += 1
            previous_sum = prefix_sum
        return count