from math import ceil

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
            
            if h < time:
                # need more per hour
                low = midpoint + 1
            else:
                # try less per hour
                high = midpoint - 1

        return low
            