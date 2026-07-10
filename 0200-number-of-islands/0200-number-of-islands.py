class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def DFS(r, c):
            if r >= m or r < 0 or c >= n or c < 0 or grid[r][c] != "1":
                return
            
            grid[r][c] = "$"
            
            DFS(r+1,c)
            DFS(r-1,c)
            DFS(r,c+1)
            DFS(r,c-1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    DFS(i,j)
                    count += 1
        return count