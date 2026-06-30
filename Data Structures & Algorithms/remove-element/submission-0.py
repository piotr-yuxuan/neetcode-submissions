class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        offset = 0

        for i in range(len(nums)):
            while i+offset < len(nums) and nums[i+offset] == val:
                offset += 1
            if len(nums) <= i+offset:
                break
            nums[i] = nums[i+offset]
        
        return len(nums) - offset