class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def is_oob(i, j):
            if i < 0 or len(image) <= i:
                return True
            elif j < 0 or len(image[0]) <= j:
                return True
            return False


        def dfs(i, j, filled):
            if is_oob(i, j) or image[i][j] != filled or image[i][j] == color:
                return

            initial = image[i][j]
            image[i][j] = color
            for (i, j) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(i, j, filled)
        
        dfs(sr, sc, image[sr][sc])
        return image