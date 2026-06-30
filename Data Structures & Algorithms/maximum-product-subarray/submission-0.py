import operator
import functools

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 == n:
            return nums[0]
        elif 2 == n:
            max(nums[0], nums[1], nums[0] * nums[1])

        max_product = positive = negative = nums[0]
        
        # Inclusive left, exclusive right.
        for i in range(1, n):
            x = nums[i]
            if 0 == x:
                positive = negative = 1
                max_product = max(max_product, 0)
            else:
                u, v = negative * x, positive * x
                positive, negative = max(u, v, x), min(u, v, x)
                max_product = max(max_product, positive)

        return max_product

    def _maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_product = 1
        for i in range(n):
            for j in range(i+1, n+1):
                max_product = max(max_product, functools.reduce(operator.mul, nums[i:j]))
        
        return max_product