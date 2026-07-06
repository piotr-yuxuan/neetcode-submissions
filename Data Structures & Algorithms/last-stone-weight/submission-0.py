import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while 1 < len(stones):
            stone1, stone2 = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if stone1 == stone2:
                continue
            heapq.heappush_max(stones, abs(stone2-stone1))
        
        return stones[0] if stones else 0