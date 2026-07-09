class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        i, j = 0, 1
        n = len(nums)
        while True:
            if nums[i%n] == nums[j%n] and i%n != j%n:
                return nums[i%n]
            i += 1 + i//n
            j += 2