from math import ceil
from bisect import bisect_right
from itertools import islice

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def metric(k):
            hours = 0
            for x in piles:
                hours += ceil(x / k)
            return hours

        low, high = 1, max(piles)
        fastest = metric(high)
        while low <= high:
            midpoint = (low+high)//2
            time = metric(midpoint)
            print(f"{low=}, {high=}, {midpoint=}, {metric(midpoint)=}")
            if h < time:
                # need more per hour
                low = midpoint + 1
            else:
                # try less per hour
                high = midpoint - 1

        return low
            