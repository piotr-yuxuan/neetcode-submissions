import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        capitalh = [] # min heap (project required capital, project index)
        for i in range(len(capital)):
            heapq.heappush(capitalh, (capital[i], i))
        
        step = 0
        eligible = [] # max heap
        while step < k:
            #print(f"{step=}, {capitalh=}, {eligible=}")
            while capitalh and capitalh[0][0] <= w:
                i = heapq.heappop(capitalh)[1]
                p = (profits[i], i)
                #print(f"Project {p=} becomes eligible")
                heapq.heappush_max(eligible, p)
            # Pick the best.
            if eligible:
                best_profit, _index = heapq.heappop_max(eligible)
                #print(f"{best_profit=}, {_index=}")
                w += best_profit
            step += 1
        
        #print(f"{step=}, {capitalh=}")
        return w