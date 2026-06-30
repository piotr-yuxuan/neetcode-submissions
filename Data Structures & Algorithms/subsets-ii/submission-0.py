class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        tmp = []

        def backtrack(i) -> None:
            if len(nums) == i:
                result.append(tmp[::])
                return

            tmp.append(nums[i])
            backtrack(i+1)            
            tmp.pop()

            # append → recurse → pop → skip duplicates → recurse again
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)

        return list(result)