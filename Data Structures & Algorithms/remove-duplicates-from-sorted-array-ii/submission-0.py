class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        def print(*args, **kwargs):
            pass
        # Inclusive both ends.
        left, right = 0, 1
        while right < len(nums):
            print(f"loop {nums}, {left=}, {right=}, {nums[left]=}, {nums[right]=}")
            if nums[left] < nums[right]:
                print(f"DEBUG 1 left+1")
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] == nums[right] and (0 == left or nums[left-1] < nums[right]):
                print(f"DEBUG 2 right+1")
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            right += 1

        print(nums)
        return left+1