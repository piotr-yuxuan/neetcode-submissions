from random import randint

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Inclusive start, exclusive end.
        def my_sort(s, e) -> None:
            if e-s+1 <= 1:
                return
            
            # Indices
            left = s
            pivot = randint(s, e-1)

            for i in range(s, pivot):
                if nums[i] < nums[pivot]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1

            old_pivot = pivot
            nums[pivot], nums[e-1] = nums[e-1], nums[pivot]

            pivot = e-1
            for i in range(old_pivot, pivot):
                if nums[i] < nums[pivot]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            
            nums[pivot], nums[left] = nums[left], nums[pivot]
            my_sort(s, left)
            my_sort(left+1, e)

        my_sort(0, len(nums))
        return nums