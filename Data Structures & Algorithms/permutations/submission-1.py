class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if 0 == len(nums):
            return []

        def dfs(i):
            if len(nums) == i:
                return [[]]

            permutations = []
            for p in dfs(i + 1):
                for j in range(len(p) + 1):
                    q = list(p)
                    q.insert(j, nums[i])
                    permutations.append(q)

            return permutations

        return dfs(0)
