class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []

        def backtracking(i, a):
            if len(nums) <= i:
                ret.append(list(a))
                return

            a.append(nums[i])
            backtracking(i+1, a)
            a.pop()

            next_i = i
            while next_i < len(nums) and nums[i] == nums[next_i]:
                next_i += 1
            backtracking(next_i, a)

        backtracking(0, [])
        return ret
