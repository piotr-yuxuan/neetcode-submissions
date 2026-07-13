class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []
        a = []

        def backtracking(i):
            if len(nums) <= i:
                ret.append(list(a))
                return

            j = i+1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            a.append(nums[i])
            backtracking(i+1)
            a.pop()
            backtracking(j)

        backtracking(0)
        return ret
