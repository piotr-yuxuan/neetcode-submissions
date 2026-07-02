from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        left = 0
        for k, v in sorted(counter.items()):
            right = left+v
            nums[left:right] = [k for _ in range(left,right)]
            left = right
