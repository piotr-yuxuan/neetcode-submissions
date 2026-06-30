class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if int(target) != target:
            return False

        known_sums = set({})
        for x in nums:
            known_sums = known_sums.union({x + y for y in known_sums})
            known_sums.add(x)
            if target in known_sums:
                return True
        return False