import heapq


class MedianFinder:
    def __init__(self):
        self.lower = []
        self.higher = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.lower, num)

        if self.higher and self.higher[0] < self.lower[0]:
            heapq.heappush(self.higher, heapq.heappop_max(self.lower))

        if 1 < len(self.lower) - len(self.higher):
            heapq.heappush(self.higher, heapq.heappop_max(self.lower))

        if 1 < len(self.higher) - len(self.lower):
            heapq.heappush_max(self.lower, heapq.heappop(self.higher))

    def findMedian(self) -> float:
        if not self.lower:
            return -1
        if not self.higher:
            return self.lower[0]

        if len(self.lower) < len(self.higher):
            return self.higher[0]
        elif len(self.higher) < len(self.lower):
            return self.lower[0]
        else:
            return (self.lower[0] + self.higher[0]) / 2
