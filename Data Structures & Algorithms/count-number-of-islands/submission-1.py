class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        unseen = {(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if "1"== grid[i][j]}

        def dfs(i, j):
            #print(f"erasing (i ,j)={(i ,j)}")
            grid[i][j] = "0"

            for (i, j) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (i, j) in unseen:
                    unseen.remove((i, j))
                    dfs(i, j)
            
        #print(len(unseen))
        while unseen:
            #print('loop' ,len(unseen))
            i, j = unseen.pop()
            #print(f"walking through (i ,j)={(i ,j)}")
            island_count += 1
            dfs(i, j)
        
        return island_count