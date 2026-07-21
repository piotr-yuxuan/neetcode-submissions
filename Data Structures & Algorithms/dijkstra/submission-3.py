import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjacency = {i: [] for i in range(n)}
        for u, v, w in edges:
            adjacency[u].append((v, w))

        h = []
        distances = {i: -1 for i in range(n)}
        heapq.heappush(h, (0, src))

        while h:
            path_weight, node = heapq.heappop(h)
            if -1 != distances[node]:
                continue

            distances[node] = path_weight
            for child, weight in adjacency[node]:
                if distances[child] == -1:
                    heapq.heappush(h, (path_weight + weight, child))

        return distances
