class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        i, j = 0, 0
        n = len(nums)
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break
        k = 0
        while i != k:
            i = nums[i]
            k = nums[k]
        return i