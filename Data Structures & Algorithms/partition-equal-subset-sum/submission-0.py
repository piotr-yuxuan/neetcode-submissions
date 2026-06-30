import operator
import functools

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = functools.reduce(operator.add, nums)
        if 1 == total % 2:
            return False

        target = total / 2

        known_sums = set({})
        for x in nums:
            new_sums = set({})
            for y in known_sums:
                new_sums.add(x + y)
            known_sums.add(x)
            known_sums = known_sums.union(new_sums)
            if target in known_sums:
                return True
        return False