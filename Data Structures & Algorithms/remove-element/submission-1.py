class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = r = 0

        for i in range(len(nums)):
            if val != nums[i]:
                k += 1
                continue
            for j in range(i+1, len(nums)):
                if val != nums[j]:
                    k += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    break        
        
        return k