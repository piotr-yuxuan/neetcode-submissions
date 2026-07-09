class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # right = read, left = write
        left = 0
        for right in nums[1:]:
            if nums[left] < right:
                left += 1
                nums[left] = right
            elif nums[left] == right and (0 == left or nums[left-1] < right):
                left += 1
                nums[left]= right

        return left+1