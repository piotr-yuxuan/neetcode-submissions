class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def dfs(i) -> None:
            nonlocal result, current

            if len(nums) == i:
                result.append(current.copy())
                return
            
            current.append(nums[i])
            dfs(i+1)
            current.pop()
            dfs(i+1)
        
        dfs(0)
        return result

