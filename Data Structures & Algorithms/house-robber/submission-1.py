import functools


class Solution:
    def rob(self, nums: List[int]) -> int:

        @functools.cache
        def dfs(i) -> int:
            if len(nums) <= i:
                return 0

            return max(
                nums[i] + dfs(i + 2),
                dfs(i + 1),
            )

        return dfs(0)
