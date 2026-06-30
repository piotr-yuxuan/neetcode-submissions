class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_first_col = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if 0 == matrix[i][j]:
                    if 0 == j:
                        zero_first_col = True
                    else:
                        matrix[0][j] = 0 # That's the j-th col except the 0th.
                    matrix[i][0] = 0 # That's for the i-th line.
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[i])-1,0,-1):
                if 0 == matrix[0][j] or 0 == matrix[i][0]:
                    matrix[i][j] = 0

        if zero_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
