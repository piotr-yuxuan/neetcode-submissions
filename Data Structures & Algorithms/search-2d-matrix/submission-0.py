from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = bisect_left(matrix, target, key=lambda x: x[-1])
        if m <= i:
            return False

        j = bisect_left(matrix[i], target)
        print(i, j)
        return target == matrix[i][j]
