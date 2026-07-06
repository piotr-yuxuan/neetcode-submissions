from heapq import heapify, heapreplace, heappushpop, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)
        self.k = k
        while self.k < len(self.heap):
            heappop(self.heap)


    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while self.k < len(self.heap):
            heappop(self.heap)

        return self.heap[0]