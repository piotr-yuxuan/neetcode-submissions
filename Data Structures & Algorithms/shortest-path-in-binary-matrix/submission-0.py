from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        border = deque([])
        seen = set ({})
        length = 0

        def is_oob(i, j):
            return i < 0 or j < 0 or len(grid) <= i or len(grid[i]) <= j
        

        def adjacent_cells(i, j):
            yield from [(i-1, j), (i+1, j)]
            yield from [(i, j-1), (i, j+1)]
            yield from [(i-1, j-1), (i-1, j+1)]
            yield from [(i+1, j-1), (i+1, j+1)]


        border.append((0, 0))
        while border:
            length += 1
            for _ in range(len(border)):
                i, j = border.popleft()
                if is_oob(i, j) or (i, j) in seen or 0 != grid[i][j]:
                    continue

                if (i, j) == (len(grid)-1, len(grid[-1])-1):
                    return length
                
                seen.add((i, j))
                for i, j in adjacent_cells(i, j):
                    border.append((i, j))
        
        return -1