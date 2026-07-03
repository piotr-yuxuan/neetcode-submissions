from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        return sorted(counter, key=counter.get, reverse=True)[:k]
