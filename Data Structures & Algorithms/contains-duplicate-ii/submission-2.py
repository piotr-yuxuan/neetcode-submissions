class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if 1 == len(nums):
            return False

        known = set()

        # Inclusive left, inclusive right
        left = 0
        for right in range(len(nums)):
            #print(f"{left=}, {right=}, {known=}, {k=}")
            if right-left-1 == k:
                known.remove(nums[left])
                left += 1
            if nums[right] in known:
                return True
            known.add(nums[right])
        
        return False