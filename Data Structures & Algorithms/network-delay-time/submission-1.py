from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = {i + 1: set() for i in range(n)}
        weights = dict()
        for u, v, t in times:
            adjacency[u].add(v)
            weights[(u, v)] = t

        h = []  # min heap
        heapq.heappush(
            h,
            (0, k),
        )

        times = dict()
        while h:
            path_weight, node = heapq.heappop(h)
            print(f"{path_weight=}, {node=}, {dict(times)=}")
            if node in times:
                continue

            if node in times:
                times[node] = min(times[node], path_weight)
            else:
                times[node] = path_weight

            for child in adjacency[node]:
                heapq.heappush(
                    h,
                    (
                        path_weight + weights[(node, child)],
                        child,
                    ),
                )

        print(times)
        return max(times.values()) if n == len(times) else -1