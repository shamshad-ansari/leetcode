class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        shapes = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, base_r, base_c, shape):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] != 1:
                return
            
            grid[r][c] = '$'
            shape.append((r-base_r, c-base_c))

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                dfs(nr,nc, base_r, base_c, shape)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = []
                    dfs(i,j, i, j, shape)
                    shapes.add(tuple(shape))
        
        return len(shapes)
    