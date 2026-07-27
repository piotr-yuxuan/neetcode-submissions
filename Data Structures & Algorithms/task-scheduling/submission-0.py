from collections import defaultdict, OrderedDict, Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []  # max heap (remaining, task)
        for task, remaining in Counter(tasks).items():
            heapq.heappush_max(h, (remaining, task))

        index = -1
        parked = deque()
        ret = 0
        while h or parked:
            index += 1
            while parked and parked[0][0] <= index:
                _, remaining, task = parked.popleft()
                heapq.heappush_max(h, (remaining, task))

            ret += 1
            if not h:
                continue

            remaining, task = heapq.heappop_max(h)
            remaining -= 1
            if 0 < remaining:
                parked.append((index+n+1, remaining, task))

        return ret