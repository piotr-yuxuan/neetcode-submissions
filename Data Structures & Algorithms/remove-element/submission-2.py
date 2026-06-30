class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = r = 0

        for i in range(len(nums)):
            if val != nums[i]:
                k += 1
                continue
            j = i+1
            while True:
                if len(nums) <= j:
                    return k
                if val != nums[j]:
                    k += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                else:
                    j += 1

        return k