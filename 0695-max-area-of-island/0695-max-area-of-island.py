class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def isValid(r,c):
            if r < 0 or c< 0 or r >= m or c >= n:
                return False
            return True

        def dfs(r,c):
            if not isValid(r,c) or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(dfs(i,j), ans)
                    
        return ans