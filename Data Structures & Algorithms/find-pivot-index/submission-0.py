from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        for i in range(1,len(prefix_sum)):
            left = prefix_sum[i-1]
            right = prefix_sum[-1] - prefix_sum[i]
            if left == right:
                return i-1
        return -1


