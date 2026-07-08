from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            remainder = target-numbers[left]
            right = bisect_left(numbers, remainder, lo=left+1)

            if right < len(numbers) and numbers[right] == remainder:
                return [left + 1, right + 1]
            
            left += 1

        return []