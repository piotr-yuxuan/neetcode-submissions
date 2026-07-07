class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        seen = set({})

        def is_oob(i, j):
            return i < 0 or j < 0 or len(grid) <= i or len(grid[i]) <= j


        def dfs(i, j):
            if is_oob(i, j):
                return
            if (i, j) in seen:
                return
            if "0" == grid[i][j]:
                return
            
            #print(f"{i=}, {j=}, {grid[i][j]=} → 0")
            grid[i][j] = "0"
            seen.add((i, j))

            for (i, j) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(i, j)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if "1" == grid[i][j]:
                    #print('\n'.join([''.join(col) for col in grid]))
                    island_count += 1
                    dfs(i, j)
        
        return island_count