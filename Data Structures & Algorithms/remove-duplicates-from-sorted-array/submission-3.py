class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if 1 == len(nums):
            return 1

        # Left = unique elements:
        # Right = cursor
        left, right = 0, 1
        while right < len(nums):
            if nums[left] < nums[right]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            right += 1
        return left+1