from collections import defaultdict
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = list(accumulate(nums))
        available = defaultdict(list)
        for i, i_sum in enumerate(prefix_sum):
                available[i_sum].append(i)

        count = 0
        previous_sum = 0
        for i in range(len(nums)):
            count += len([x for x in available.get(k + previous_sum, []) if i <= x])
            previous_sum = prefix_sum[i]
        return count