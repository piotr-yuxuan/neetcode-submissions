from itertools import accumulate

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [list(accumulate(matrix[0]))]
        for i in range(1, len(matrix)):
            row_prefix_sum = list(accumulate(matrix[i]))
            prefix_sum = []
            for j in range(len(matrix[i])):
                prefix_sum.append(row_prefix_sum[j] + self.prefix[-1][j])
            self.prefix.append(prefix_sum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.prefix[row1-1][col2] if row1 else 0
        left = self.prefix[row2][col1-1] if col1 else 0
        corner = self.prefix[row1-1][col1-1] if row1 and col1 else 0
        return self.prefix[row2][col2] - top - left + corner
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)