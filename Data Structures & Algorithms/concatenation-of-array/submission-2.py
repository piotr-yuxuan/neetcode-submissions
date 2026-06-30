from itertools import cycle, islice

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return list(islice(cycle(nums), 2*len(nums)))