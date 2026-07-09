class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # Inclusive both ends.
        left, right = 0, 1
        while right < len(nums):
            if nums[left] < nums[right]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] == nums[right] and (0 == left or nums[left-1] < nums[right]):
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            right += 1

        return left+1