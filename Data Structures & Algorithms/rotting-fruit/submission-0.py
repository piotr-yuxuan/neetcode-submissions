from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        border = deque([])
        visited = set({})
        fresh = set({})
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if 1 == grid[i][j]:
                    fresh.add((i, j))
                elif 2 == grid[i][j]:
                    border.append((i, j))

        def is_oob(i, j):
            return (i < 0 or j < 0 or len(grid) <= i or len(grid[i]) <= j)

        time = 0
        while border:
            for _ in range(len(border)):
                (i, j) = border.popleft()
                grid[i][j] = 2
                if (i, j) in fresh:
                    fresh.remove((i, j))
                if not fresh:
                    return time
                for i, j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if is_oob(i, j) or (i, j) in visited or (i, j) not in fresh:
                        continue
                    visited.add((i, j))
                    border.append((i, j))
            #print(f"{time=}, {border=}")
            time += 1
        #print(f"end {visited=}, {fresh=}")
        
        return -1 if fresh else time
