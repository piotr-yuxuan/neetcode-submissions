from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if 0 == len(nums):
            return nums[k]
        
        # Exclusive end.
        def partition(s, e) -> int:
            index = randint(s, e-1)
            nums[index], nums[e-1] = nums[e-1], nums[index]

            pivot = e-1
            left = s
            for i in range(s, pivot):
                if nums[i] < nums[pivot]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            nums[left], nums[pivot] = nums[pivot], nums[left]
            return left

        s = 0
        e = len(nums)
        pivot = -1

        while pivot != len(nums)-k:
            pivot = partition(s, e)
            if pivot < len(nums)-k:
                s = pivot+1
            else:
                e = pivot
        
        print(nums, pivot)
        return nums[pivot]