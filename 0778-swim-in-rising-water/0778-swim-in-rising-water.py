class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def isPossible(level):
            visited = set()
            def DFS(i, j):
                if (
                    i < 0 or i >= n or
                    j < 0 or j >= n or
                    grid[i][j] > level or
                    (i, j) in visited
                ):
                    return False

                if i == n-1 and j == n-1:
                    return True
                
                visited.add((i,j))

                return (
                    DFS(i+1, j) or
                    DFS(i-1, j) or
                    DFS(i, j+1) or
                    DFS(i, j-1)
                )

            return DFS(0,0)

        n = len(grid)
        start = 0
        end = max(max(row) for row in grid)
        ans = -1
        while start <= end:
            mid  = start + (end-start)//2

            if isPossible(mid):
                ans = mid
                end = mid -1
            else:
                start = mid + 1
        return ans