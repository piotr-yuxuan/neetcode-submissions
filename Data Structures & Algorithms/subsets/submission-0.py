class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        work = []

        def backtrack(i) -> None:
            if len(nums) == i:
                result.append(work[::])
                return

            backtrack(i+1)
            work.append(nums[i])
            backtrack(i+1)
            work.pop()
        
        backtrack(0)

        return result
