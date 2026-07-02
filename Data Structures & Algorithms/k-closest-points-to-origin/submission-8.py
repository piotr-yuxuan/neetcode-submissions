from functools import cache

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        def metric(p) -> int:
            return p[0]**2 + p[1]**2

        # Stateful. Inclusive start, exclusive end.
        def partition(s, e):
            left = s
            pivot = e-1

            m = metric(points[pivot])
            for i in range(s, pivot):
                if metric(points[i]) < m:
                    points[i], points[left] = points[left], points[i]
                    left += 1
            points[pivot], points[left] = points[left], points[pivot]

            return left
        
        s, e = 0, len(points)
        pivot = -1

        while pivot != k:
            pivot = partition(s, e)
            if pivot < k:
                s = pivot+1
            else:
                e = pivot
        
        return points[:k]
