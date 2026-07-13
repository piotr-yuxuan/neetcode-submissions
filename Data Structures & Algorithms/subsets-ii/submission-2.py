class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ret = []
        prefix = set()

        def backtracking(i, a):
            if len(nums) <= i:
                ret.append(list(a))
                return

            a.append(nums[i])
            t = tuple(sorted(a))
            if t not in prefix:
                prefix.add(t)
                backtracking(i + 1, a)
            a.pop()
            backtracking(i + 1, a)

        backtracking(0, [])
        return ret
