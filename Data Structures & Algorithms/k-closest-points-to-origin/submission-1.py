from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p) -> int:
            return sqrt(p[0]**2 + p[1]**2)
        return sorted(points, key=distance)[:k]