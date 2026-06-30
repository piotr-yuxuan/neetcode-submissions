def solution(input: List[int], target: int):
    seen = dict()
    for i, j in enumerate(input):
        if target - j in seen:
            return [seen[target - j], i]
        else:
            seen[j] = seen.setdefault(j, i)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return solution(nums, target)        