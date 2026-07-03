class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        current_sum = 0

        def dfs(i) -> None:
            nonlocal current_sum

            if target < current_sum:
                return
            if target == current_sum:
                result.append(current[::])
                return
            if len(nums) == i:
                return
            
            current.append(nums[i])
            current_sum += nums[i]
            dfs(i)
            current.pop()
            current_sum -= nums[i]
            dfs(i+1)
            return
        
        dfs(0)
        return result