from itertools import accumulate
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = list(accumulate(nums, operator.mul))
        right = list(accumulate(reversed(nums), operator.mul))
        print(f"{left=}")
        print(f"{right=}")
        return [(left[i-1] if 0 <= i-1 else 1) * (right[n-2-i] if 0 <= n-2-i else 1) for i in range(n)]
        