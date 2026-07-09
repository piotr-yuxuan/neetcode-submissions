from itertools import accumulate
import operator


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] + list(accumulate(nums, operator.mul))
        right = [1] + list(accumulate(reversed(nums), operator.mul))
        return [left[i] * right[n - 1 - i] for i in range(n)]
