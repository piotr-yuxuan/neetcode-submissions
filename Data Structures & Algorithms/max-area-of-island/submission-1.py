class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        unseen = {(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if 1 == grid[i][j]}

        def dfs(i, j) -> area:
            grid[i][j] = 0

            area = 1
            for (i, j) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (i, j) in unseen:
                    unseen.remove((i, j))
                    area += dfs(i, j)
            return area
            
        max_area = 0
        while unseen:
            i, j = unseen.pop()
            max_area = max(max_area, dfs(i, j))
        
        return max_area