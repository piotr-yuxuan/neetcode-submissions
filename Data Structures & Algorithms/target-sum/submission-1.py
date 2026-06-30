import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        diff = sum(nums) - target
        if diff < 0 or 1 == diff % 2:
            return 0

        # previous, current
        p = dict({0: 1})
        
        for n in nums:
            c = dict({})
            for j, v in p.items():
                c[j + n] = c.get(j + n, 0) + v
                c[j - n] = c.get(j - n, 0) + v
            p = c
        return c.get(target, 0)
