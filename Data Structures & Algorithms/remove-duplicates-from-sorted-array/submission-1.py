class Solution:
    def _removeDuplicates(self, nums: List[int]) -> int:
        unique_items = 1
        offset = 0

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                offset += 1
            else:
                unique_items += 1

            nums[i-offset] = nums[i]
        else:
            return unique_items

    def removeDuplicates(self, nums: List[int]) -> int:
        unique_items = 1
        offset = 0
        
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                offset += 1
            else:
                unique_items += 1

            nums[i-offset] = nums[i]
            i += 1
        else:
            return unique_items
