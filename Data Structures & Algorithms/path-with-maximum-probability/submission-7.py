import heapq


class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:
        adjacency = {i: list() for i in range(n)}
        frontier = {i: 0 for i in range(n)}
        frontier[start_node] = 1
        for i in range(len(edges)):
            node, child = edges[i]
            weight = succProb[i]
            adjacency[node].append((child, weight))
            adjacency[child].append((node, weight))

        print(f"{frontier=}")
        print(f"{adjacency=}")

        h = []  # max heap
        heapq.heappush_max(
            h,
            (
                1,
                start_node,
            ),
        )

        while h:
            path_weight, node = heapq.heappop_max(h)

            if end_node == node:
                return path_weight
            if path_weight < frontier[node]:
                continue

            for child, weight in adjacency[node]:
                if frontier[child] < path_weight * weight:
                    frontier[child] = path_weight * weight
                    heapq.heappush_max(h, (path_weight * weight, child))

        return 0
